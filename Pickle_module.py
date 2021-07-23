import pickle

# Pickling a object
cars = ["Audi", "BMW", "Ferrari", "RangeRover"]
with open("mycar.pkl", "wb") as file:
    pickle.dump(cars, file)
file.close()

with open("mycar.pkl", "rb") as file:
    print(pickle.load(file))

file.close()
