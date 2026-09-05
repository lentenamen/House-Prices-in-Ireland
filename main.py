import pandas as pd
import numpy as np

"""
read csv to dataframe
cp1252 used for the € sign
"""
def read_csv():
    df = pd.read_csv(
        "data/raw/PPR-ALL.csv",
        encoding="cp1252",
        quotechar='"',
        low_memory=False
    )


    return df

df = read_csv()

df = df.rename(columns={
    "Date of Sale (dd/mm/yyyy)": "date",
    "Address": "address",
    "County": "county",
    "Eircode": "eircode",
    "Price (€)": "price",
    "Not Full Market Price": "not_full_market_price",
    "VAT Exclusive": "vat_exclusive",
    "Description of Property": "property_type",
    "Property Size Description": "property_size"
})

print(df["county"].head())
print(df["eircode"].head())
print(df["price"].head())
