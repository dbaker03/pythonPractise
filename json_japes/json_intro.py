import json
# key-value pairs

cars = {
    "make": "Toyota",
    "model": "Yaris",
    "fuel": "Petrol",
    "mpg": 30,
    "driver": None
}

print(cars, type(cars))
print(cars["fuel"])

dumps = json.dumps(cars)
print(dumps, type(dumps))
# .dumps() will convert it to a string

with open("Tonya.json", 'w') as json_file:
    json.dump(cars, json_file)
# we can use .dump() to get it to write it straight into a file


# we car .load() and .loads() - create an object or create a string
with open("spratan.json") as json_file:
    spartan = json.load(json_file)

print(spartan)


