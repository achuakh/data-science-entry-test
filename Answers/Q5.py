def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # check if first num and second number is interger or float
    
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1  # Return -1 for non-numeric input
    if divisor == 0:
        return -1 # Return -1 if the divisor is zero.
    return num % divisor == 0  # modulo operator to check


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

number1 = 10
divisor1 = 2
result1 = check_divisibility(number1, divisor1)
print(f"{number1} is divisible by {divisor1}: {result1}")

number1 = 7
divisor1 = 3
result1 = check_divisibility(number1, divisor1)
print(f"{number1} is divisible by {divisor1}: {result1}")

