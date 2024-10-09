import pandas as pd

dtype_dict = {18: str, 29: str, 38: str, 40: str, 41: str, 42: str}

df = pd.read_csv(
    "files/Parking_Violations_Issued_-_Fiscal_Year_2015.csv",
    dtype=dtype_dict,
    parse_dates=["Issue Date"],
)

print(df.head())
print(df.dtypes)

df.to_parquet("../files/Parking_Violations_Issued_-_Fiscal_Year_2015.parquet")
