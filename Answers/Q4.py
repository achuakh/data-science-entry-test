def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    # check for non-string input
    if not isinstance(s, str):
        return -1
    #create a variable called reversed_string
    reversed_string = ""

    # go char one by one and fill in reverse and return output
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# use these string and create variables
string1 = "Hello World"
string2 = "Python"

# created the reversed variables
reversed1 = string_reverse(string1)
reversed2 = string_reverse(string2)

# print them
print(f"Original string: {string1}")
print(f"Reversed string: {reversed1}")

print(f"Original string: {string2}")
print(f"Reversed string: {reversed2}")