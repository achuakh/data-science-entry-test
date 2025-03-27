def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # check if there's an existing key by that name of value in dct and print
    
    if key in dct:
        original_value = dct[key]
        print(f"Original value: {original_value}") #optional
        dct[key] = value
    # create the key if it's not existing    
    else:
        dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# create variable dict with Alice and age of 25
dict = {"name": "Alice", "age": 25}

# update the age to 26
updated_dict1 = update_dictionary(dict, "age", 26)

# print output
print(f"Updated to: {updated_dict1}")
