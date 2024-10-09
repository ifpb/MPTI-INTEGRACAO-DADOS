import pandas as pd

df = pd.read_orc(
    "../files/equities.orc", columns=["symbol", "name", "currency", "exchange"]
)

print(df.head())
