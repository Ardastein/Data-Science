from data_preparation import load_and_prepare_data
from visualization import plot_time_series, plot_correlation_matrix, plot_moving_averages

def main():
    file_path = 'data/Meta.csv'
    
    df = load_and_prepare_data(file_path)
    
    plot_time_series(df, 'Close')
    
    plot_correlation_matrix(df)
    
    plot_moving_averages(df, 'Close')

if __name__ == "__main__":
    main()
