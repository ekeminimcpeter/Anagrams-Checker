# Author: Ekemini Peter
# Date: 17/12/2024
# Revision: 1
# Description: Original Implementation of Anagrams Checker
# Scope:
#   Ask the user for two separate texts
#   Checks whether, the entered texts are anagrams and prints the result
#   Assume that two empty strings are not anagrams
#   Treat upper- and lower-case letters as equal
#   Spaces are not taken into account during the check – treat them as non-existent
#   Numbers are treated as valid characters.
#   Thanks to ChatGPT for colaborative insight to improved code
##################################################################################################################

def is_anagrams(text_1,text_2):
    # Normalise the inputs: remove white spaces, convert to uppercase
    normalised_text_1 = text_1.replace(" ","").upper()
    normalised_text_2 = text_2.replace(" ","").upper()

    ## Check if the characters of input strings are equal
    # Empty strings are not anagrams
    if not normalised_text_1 or not normalised_text_2: # Deals with white spaced string
        return False
    # Sort, joint: convert to string, and compare
    return ''.join(sorted(normalised_text_1)) == ''.join(sorted(normalised_text_2))

# Ask the user for two separate texts
first_text = input("Enter your first text: ")
second_text = input("Enter your Second text: ")

# Prevent user from providing empty strings and numbers
if first_text and second_text:
    if is_anagrams(first_text,second_text):
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Error: an empty input was provided!")

