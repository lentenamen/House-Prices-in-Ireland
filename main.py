import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/raw/PPR-ALL.csv",
    encoding="cp1252"
)

print(df.head())
print(df["Address"].head())
print(df["County"].head())
print(df["Eircode"].head())