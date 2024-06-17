import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole_weight',
                    'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'Rings']
    data = pd.read_csv(file_path, names=column_names)
    return data

def preprocess_data(data):
    data['Sex'] = data['Sex'].map({'M': 0, 'F': 1, 'I': 2})

    numeric_cols = ['Length', 'Diameter', 'Height', 'Whole_weight', 
                    'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'Rings']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    return data

def visualize_data(data):
    print(data.describe())
    
    print(data.dtypes)
    
    print(data.columns)

    numeric_cols = ['Length', 'Diameter', 'Height', 'Whole_weight', 
                    'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'Rings']
    for col in numeric_cols:
        if col not in data.columns:
            print(f"Column {col} not found in data!")
    
    sns.pairplot(data[numeric_cols])
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(x='Sex', data=data)
    plt.title('Cinsiyet Dağılımı')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(data['Rings'], kde=True, bins=30)
    plt.title('Yüzük Dağılımı (Yaş)')
    plt.xlabel('Yüzük Sayısı')
    plt.ylabel('Frekans')
    plt.show()

if __name__ == "__main__":
    data = load_data('data/abalone1.data.txt')
    data = preprocess_data(data)  
    visualize_data(data)
