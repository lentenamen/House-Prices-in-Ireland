from data_loader import load_data 
from preprocessing import standardize
from analysis import analysis
from visualization import visualisation1

def main():
    # Path to the raw dataset
    file_path = "data/raw/PPR-ALL.csv"

    # Load the data 
    df = load_data(file_path)
    if df is None:
        print("Failed to load the data")
        return 
    df = standardize(df)
    annual = analysis(df)
    visualisation1(annual)

    
if __name__ == "__main__":
    main()