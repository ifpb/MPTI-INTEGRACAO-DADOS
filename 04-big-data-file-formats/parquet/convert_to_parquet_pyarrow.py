import pyarrow.csv as pv
import pyarrow.parquet as pq

file_location = "../files/equities.csv"

table = pv.read_csv(file_location)
pq.write_table(table, "../files/equities-2.parquet")
