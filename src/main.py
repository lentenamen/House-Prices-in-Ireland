from data_loader import load_data 
from preprocessing import standardize

def main():
    # Path to the raw dataset
    file_path = "data/raw/PPR-ALL.csv"

    # Load the data 
    df = load_data(file_path)
    df = standardize(df)
    print(df.head())

    if df is None:
        print("Failed to load the data")
        return 
    
if __name__ == "__main__":
    main()