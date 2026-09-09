import pandas as pd
import numpy as np

def standardize(df):
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
    

    df["date"] = pd.to_datetime(df["date"],format="%d/%m/%Y",errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    df["county"] = df["county"].str.strip().str.lower()

    df["price"] = pd.to_numeric(
        df["price"]
        .str.replace("€", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    df.columns = df.columns.str.lower().str.strip()
    df = df.drop_duplicates()

    return df