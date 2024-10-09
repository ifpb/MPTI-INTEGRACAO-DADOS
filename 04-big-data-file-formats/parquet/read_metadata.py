from pyarrow import parquet as pq

file_info = pq.ParquetFile("../files/equities-2.parquet")
#file_info = pq.ParquetFile("../files/Parking_Violations_Issued_-_Fiscal_Year_2015.parquet")


print("--- METADATA ---")
print(file_info.metadata)
# --- METADATA ---
# <pyarrow._parquet.FileMetaData object at 0x1018f6200>
#   created_by: parquet-cpp-arrow version 14.0.1
#   num_columns: 20
#   num_rows: 158647
#   num_row_groups: 1
#   format_version: 2.6
#   serialized_size: 4318

print("")
print(file_info.schema)
# <pyarrow._parquet.ParquetSchema object at 0x1018f9480>
# required group field_id=-1 schema {
#   optional binary field_id=-1 symbol (String);
#   optional binary field_id=-1 name (String);
#   optional binary field_id=-1 summary (String);
#   optional binary field_id=-1 currency (String);
#   optional binary field_id=-1 sector (String);
#   optional binary field_id=-1 industry_group (String);
#   optional binary field_id=-1 industry (String);
#   optional binary field_id=-1 exchange (String);
#   optional binary field_id=-1 market (String);
#   optional binary field_id=-1 country (String);
#   optional binary field_id=-1 state (String);
#   optional binary field_id=-1 city (String);
#   optional binary field_id=-1 zipcode (String);
#   optional binary field_id=-1 website (String);
#   optional binary field_id=-1 market_cap (String);
#   optional binary field_id=-1 isin (String);
#   optional binary field_id=-1 cusip (String);
#   optional binary field_id=-1 figi (String);
#   optional binary field_id=-1 composite_figi (String);
#   optional binary field_id=-1 shareclass_figi (String);
# }
