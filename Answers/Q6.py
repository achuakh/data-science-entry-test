def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    # check if lst is of list type, if not return -1
    if not isinstance(lst, list):
        return -1
    # reset the index counter to 0
    index = 0
    # count from 0 and check if the number in index of lst is less than 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    return "No negatives"
    

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

numbers1 = [3, 5, -1, 7, -2, 8]
numbers2 = [2, 10, 7, 0]

first_negative1 = find_first_negative(numbers1)
first_negative2 = find_first_negative(numbers2)

print(f"First negative in {numbers1}: {first_negative1}")
print(f"First negative in {numbers2}: {first_negative2}")