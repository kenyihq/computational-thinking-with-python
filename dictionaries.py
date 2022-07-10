# Dictionaries or hash


from traceback import print_tb


my_dict = {
    "David":35,
    "Erika":32,
    "Jaime":50,
    "Kenyi":28
}


# Exist
print(my_dict["Kenyi"])

# Not exist

print(my_dict.get("Julberth", "No esxite"))

# Change value
my_dict["Kenyi"] = 20
print(my_dict)

# Delete item
del my_dict["Kenyi"]
print(my_dict)

# Iterator

for k in my_dict.keys():
    print(k)

for v in my_dict.values():
    print(v)

for k, v in my_dict.items():
    print(k, v)

# Validate value

print("Kenyi" in my_dict)
print("David" in my_dict)


# Dict comprehensions

dict_comprehension = {i:i**3 for i in range(1, 11) if i%3 != 0}

print(dict_comprehension)