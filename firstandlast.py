def sum_of_first_and_last_digit(n):
    # Convert the integer to a string to easily access its digits
    n_str = str(n)

    # Check if the integer is non-negative
    if n >= 0:
        # Get the first and last digits as integers
        first_digit = int(n_str[0])
        last_digit = int(n_str[-1])

        # Calculate the sum of the first and last digits
        digit_sum = first_digit + last_digit

        return digit_sum
    else:
        # Handle negative integers by making them positive and then finding the sum
        n = abs(n)
        return sum_of_first_and_last_digit(n)

# Input a number from the user
number = int(input("Enter an integer: "))

# Calculate and print the sum of the first and last digits
result = sum_of_first_and_last_digit(number)
print("The sum of the first and last digits is:", result)
