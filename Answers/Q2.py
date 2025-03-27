def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # checking if not a list
    if not isinstance(lst, list):
        return -1  # Return -1 if lst is not a list
    
    # search from input lst for find_val and then replace it with replace_val
    else:
        modified_list = [replace_val if val == find_val else val for val in lst]
        return modified_list

    return

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

input_list = [1, 2, 3, 4, 2, 2]
output_list = find_and_replace(input_list, 2, 5)
print(f"Original list: {input_list}")
print(f"Modified list: {output_list}")

input_list = ["apple", "banana", "apple"]
output_list = find_and_replace(input_list, "apple", "orange")
print(f"Original list: {input_list}")
print(f"Modified list: {output_list}")

