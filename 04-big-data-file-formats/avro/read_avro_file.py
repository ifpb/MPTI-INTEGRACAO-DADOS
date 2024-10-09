from fastavro import reader

with open("../files/countries-worldbank.avro", "rb") as f:
    for country in reader(f):
        print(country)
