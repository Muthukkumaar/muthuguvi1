def find_minimum_element(input_list):
    if all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1)):
        # The list is already sorted in ascending order
        return input_list[0]
    else:
        # The list is not sorted, so find the minimum using the min() function
        return min(input_list)

# Example usage:
sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [5, 3, 8, 1, 7]

min_element_sorted = find_minimum_element(sorted_list)
min_element_unsorted = find_minimum_element(unsorted_list)

print("Minimum element in sorted list:", min_element_sorted)
print("Minimum element in unsorted list:", min_element_unsorted)
