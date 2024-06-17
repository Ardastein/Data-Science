import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

base_dir = 'C:/Users/HP/Desktop/Missions/Huawei/Biology/Leaf Veins Voronoi Diagrams'
data_dir = os.path.join(base_dir, 'data')
results_dir = os.path.join(base_dir, 'results')
voronoi_dir = os.path.join(results_dir, 'voronoi_diagrams')
plots_dir = os.path.join(results_dir, 'plots')

os.makedirs(voronoi_dir, exist_ok=True)
os.makedirs(plots_dir, exist_ok=True)

image_files = ['images.jpg', 'leaves-5424297_1280.content.jpg']
images = []
for file in image_files:
    file_path = os.path.join(data_dir, file)
    image = cv2.imread(file_path)
    if image is None:
        print(f"Error loading image: {file_path}")
    images.append(image)

if any(image is None for image in images):
    print("Some images could not be loaded. Please check the file paths and try again.")
    exit()

gray_images = [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

edges = [cv2.Canny(gray, 50, 150) for gray in gray_images]

contours_list = [cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0] for edge in edges]

for idx, contours in enumerate(contours_list):
    points = np.vstack([cnt.squeeze() for cnt in contours if len(cnt.squeeze().shape) == 2])
    
    if points.shape[0] < 4:
        print(f"Not enough points to generate Voronoi diagram for image {image_files[idx]}")
        continue
    
    vor = Voronoi(points)
    
    plt.figure(figsize=(10, 10))
    voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=2, line_alpha=0.6, point_size=2)
    plt.scatter(points[:, 0], points[:, 1], s=1, color='blue')
    plt.title(f'Voronoi Diagram for {image_files[idx]}')
    plt.gca().invert_yaxis()
    
    plot_path = os.path.join(voronoi_dir, f'voronoi_{idx}.png')
    plt.savefig(plot_path)
    plt.close()

    original_image = images[idx].copy()
    cv2.drawContours(original_image, contours, -1, (0, 255, 0), 2)
    original_with_contours_path = os.path.join(plots_dir, f'contours_{idx}.png')
    cv2.imwrite(original_with_contours_path, original_image)

    edges_path = os.path.join(plots_dir, f'edges_{idx}.png')
    cv2.imwrite(edges_path, edges[idx])

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(images[idx], cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(edges[idx], cmap='gray')
    plt.title('Edges')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Contours')
    plt.axis('off')

    plt.suptitle(f'Analysis for {image_files[idx]}')
    combined_path = os.path.join(plots_dir, f'combined_{idx}.png')
    plt.savefig(combined_path)
    plt.close()
