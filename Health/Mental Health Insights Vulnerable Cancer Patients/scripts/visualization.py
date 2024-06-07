import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(model, feature_names, output_path):
    importance = model.feature_importances_
    sorted_idx = importance.argsort()
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(sorted_idx)), importance[sorted_idx], align='center')
    plt.yticks(range(len(sorted_idx)), feature_names[sorted_idx])
    plt.title('Feature Importance')
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    print("Feature importance plot saved to results/model_results/")
