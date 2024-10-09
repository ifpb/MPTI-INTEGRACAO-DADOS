import pandas as pd 

df = pd.read_csv('../files/equities.csv')

print(df.head())

df.to_parquet('../files/equities.parquet')
