# Define three lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [6, 7, 8, 9, 10]

# Find duplicates by converting the lists to sets and using the intersection method
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find duplicates within the three lists
common_elements = set1.intersection(set2, set3)

# Convert the common elements set back to a list
duplicates = list(common_elements)

# Print the duplicates
print("Duplicates:", duplicates)
