def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

# Your list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count the happy numbers in the list
happy_numbers = [num for num in numbers if is_happy_number(num)]
count = len(happy_numbers)

print(f"Happy numbers in the list: {happy_numbers}")
print(f"Number of happy numbers: {count}")
