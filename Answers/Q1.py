def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    # check for either NOT integer
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1  # Return -1 if either not numeric
    # perform the swap
    else:
        # Swap the values around
        x, y = y, x
        print(f"Swapped value: x = {x}, y = {y}") #print the swapped values
        return None 
    return

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

output = swap("Apple", 10)
print (output)
output = swap(9,17)
print (output)

# test

