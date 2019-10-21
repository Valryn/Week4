def factorial(input):
    """This function only supports positive numbers. Takes a number and returns its factorial """
    input = abs(input)
    if input is 1:
        return 1;
    else:
        return input * factorial(input-1)

print(factorial(-5))