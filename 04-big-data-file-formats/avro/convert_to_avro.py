import json

from fastavro import writer, parse_schema

with open("countries-schema.avsc", "r") as schema_file:
    countries_schema = json.load(schema_file)
    parsed_schema = parse_schema(countries_schema)

with open("../files/countries-worldbank.json", "r") as countries_file:
    countries_data = json.load(countries_file)

with open("../files/countries-worldbank.avro", "wb") as countries_avro:
    writer(countries_avro, parsed_schema, countries_data)
