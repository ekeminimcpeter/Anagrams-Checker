# Author: Ekemini Peter
# Date: 15/12/2024
# Revision: 0
# Description: Original Implementation of Anagrams Checker
# Scope:
#   Ask the user for two separate texts
#   Checks whether, the entered texts are anagrams and prints the result
#   Assume that two empty strings are not anagrams
#   Treat upper- and lower-case letters as equal
#   Spaces are not taken into account during the check – treat them as non-existent

##################################################################################################################

def is_anagrams(text_1,text_2):
    # Normalise the inputs: remove white spaces, convert to uppercase
    normalised_text_1 = text_1.replace(" ","").upper()
    normalised_text_2 = text_2.replace(" ","").upper()

    # Check if the characters of input strings are equal
    if len(normalised_text_1) == 0 and len(normalised_text_2) == 0: # Check if the characters are only white spaces
        result = False
    elif len(normalised_text_1) == len(normalised_text_2):  # Check if number of characters are equal
        # Check if a character appears in both strings
        for char in normalised_text_2: # Compare text_2 characters with text_1
            result = char in normalised_text_1
    else:
        result = len(normalised_text_1) == len(normalised_text_2) # Return a logical result of 
    return result

# Ask the user for two separate texts
first_text = input("Enter your first text: ")
second_text = input("Enter your Second text: ")

# Prevent user from providing empty strings
if first_text and second_text != "":
    if is_anagrams(first_text,second_text):
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Error: an empty input was provided!")

