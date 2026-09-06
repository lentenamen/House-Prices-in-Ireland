import pandas as pd
import numpy as np

def standardize(df):
    df.columns = df.columns.str.lower().str.strip()
    df = df.drop_duplicates()

    
