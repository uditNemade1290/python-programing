#Dictionary Operations

# 4.1 Create and access dictionary elements
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])

# 4.2 Update dictionary
my_dict["age"] = 26
print("Updated dictionary:", my_dict)

# 4.3 Remove dictionary elements
del my_dict["age"]
print("After deletion:", my_dict)

# 4.4 Merging dictionaries
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
merged_dict = {**dict_a, **dict_b}
print("Merged dictionary:", merged_dict)
