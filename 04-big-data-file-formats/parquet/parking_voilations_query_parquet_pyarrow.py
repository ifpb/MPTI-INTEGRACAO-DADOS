from datetime import datetime

import pandas as pd

file_location = "../files/Parking_Violations_Issued_-_Fiscal_Year_2015.parquet"

start_dt = datetime(2015, 1, 1)
end_dt = datetime(2015, 2, 1)
df = pd.read_parquet(
    file_location,
    engine="pyarrow",
    columns=["Issue Date", "Vehicle Make"],
    filters=[[("Issue Date", ">=", start_dt), ("Issue Date", "<", end_dt)]],
)

print(df.head())

### GET TOTAL VIOLATIONS BY VEHICLE MAKE FOR MONTH OF JANUARY ###

# Group by 'Vehicle Make' and count tickets
ticket_counts = df.groupby("Vehicle Make").size()

# Drop counts less than 100 (assuming this is bogus data)
ticket_counts = ticket_counts[ticket_counts >= 1000]

# The result is a Series with 'Vehicle Make' as the index and ticket counts as the values
print(ticket_counts)
