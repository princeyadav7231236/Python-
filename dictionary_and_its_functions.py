# d1 = {}  # Empty Dictionary
# print(d1)

dict1 = {"Name":"Diwakar singh", "Class":"XII", "Profession":{"Profession":"Teacher", "profession":"Student"}, "Dream":"To become a XR Developer", "Favorite game":"Cricket", "Hobby":"Reading"}
dict1["Favorite game"] = "Football"
del dict1["Hobby"]
print(dict1["Profession"]["profession"])
# print(dict1)
dict2 = dict1.copy()
print(dict2)
dict2.update({"name":"DEVIL"})
print(dict2)
print(dict2.keys())
print(dict2.keys())
print(dict2.values())
# print(dict1)
