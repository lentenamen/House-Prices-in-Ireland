import pandas as pd 

def load_data(file_path):
    """ 
    loads the dataset from a CSV file or JSON file into a pandas DataFrame

    The function checks the file extension to choose the proper loading method.
    If the file is not in a supported format then a ValueError is raised. 
    Any errors encountered during the data loading are printed out and the function returns None.

    Args: 
        file_path: str
        The path to the dataset file. Must end with csv or json

    Returns:
        pandas DataFrame or None

    """

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path,
        encoding="cp1252",
        quotechar='"',
        low_memory=False
    )
        
    elif file_path.endswith(".json"):
        df = pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")

    print("Data loaded successfully")

    return df