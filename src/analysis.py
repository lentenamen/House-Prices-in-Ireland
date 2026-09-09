import pandas as pd
import numpy as np


def analysis(df):
    print(f'Rows:     {len(df):,}')
    print(f'Columns:  {df.shape[1]}')
    print(f'Date range: {df["date"].min().date()} -> {df["date"].max().date()}')

    stats = df['price'].describe(percentiles=[.1, .25, .5, .75, .9])
    labels = ['Min', '10th %ile', '25th %ile', 'Median', '75th %ile', '90th %ile', 'Max']
    values = [stats['min'], stats['10%'], stats['25%'], stats['50%'], stats['75%'], stats['90%'], stats['max']]

    print('National price distribution (all years):')
    print('-' * 35)
    for l, v in zip(labels, values):
        print(f'  {l} €{v:.0f}')
    print(f'\n  Mean        €{df["price"].mean():.0f}')
    print(f'  Std dev     €{df["price"].std():.0f}')

    annual = df.groupby('year').agg(
    median_price=('price', 'median'),
    mean_price=('price', 'mean'),
    total_sales=('price', 'count'),
    total_value=('price', 'sum')
    ).reset_index()

    annual['yearly_percentage_change'] = annual['median_price'].pct_change() * 100

    return annual