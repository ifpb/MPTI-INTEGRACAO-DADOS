import pandas as pd
from pyarrow import parquet as pq

file_location = "../files/Parking_Violations_Issued_-_Fiscal_Year_2015.parquet"
file_info = pq.ParquetFile(file_location)

print(file_info.metadata)
print(file_info.schema)

df = pd.read_parquet(file_location, columns=["Issue Date", "Vehicle Make"])

print(df.head())

### GET TOTAL VIOLATIONS BY VEHICLE MAKE FOR MONTH OF JANUARY ###

# Filter for January 2015
jan_2015 = df[(df["Issue Date"] >= "2015-01-01") & (df["Issue Date"] < "2015-02-01")]

# Group by 'Vehicle Make' and count tickets
ticket_counts = jan_2015.groupby("Vehicle Make").size()

# Drop counts less than 100 (assuming this is bogus data)
ticket_counts = ticket_counts[ticket_counts >= 1000]

# The result is a Series with 'Vehicle Make' as the index and ticket counts as the values
print(ticket_counts)
