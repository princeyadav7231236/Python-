import json

data = '{"var1" : "Devil", "var2": 420}'
print(data)  # Output --> {"var1" : "Devil", "var2": 420}

parsed = json.loads(data)
print(parsed)  # Output --> {'var1': 'Devil', 'var2': 420}
print(parsed["var1"])

data_2 = {
    "Name": "Devil",
    "cars": ['BMW', 'RollsRoyal'],
    "Fridge": ("Ice cream", "Fruits", "Milk"),
    "var": False
}
obj_1 = json.dumps(data_2)
print(obj_1)
# Output -->  {"Name": "Devil", "cars": ["BMW", "RollsRoyal"], "Fridge": ["Ice cream", "Fruits", "Milk"], "var": false}


