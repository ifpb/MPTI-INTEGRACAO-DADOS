import json

from fastavro.validation import validate_many

with open("countries-schema.avsc", "r") as schema_file:
    countries_schema = json.load(schema_file)

with open("../files/countries-worldbank.json", "r") as countries_file:
    countries_data = json.load(countries_file)

validate_many(countries_data, countries_schema)

# test schema with invalid data
invalid_data = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3}]

# fastavro._validate_common.ValidationError
validate_many(invalid_data, countries_schema)
