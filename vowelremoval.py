def remove_vowels(input_string):
    # Define a string containing all the vowels in both uppercase and lowercase
    vowels = "aeiou"
    
    # Initialize an empty string to store the result
    result_string = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a vowel and add it to the result
        if char not in vowels:
            result_string += char
    
    return result_string

#Input

input_string = "Muthukkumaar"
result = remove_vowels(input_string)
print(result)  

