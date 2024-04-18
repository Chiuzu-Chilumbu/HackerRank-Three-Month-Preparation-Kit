"""
Challenge: A pangram is a string that contains every letter of the alphabet. 
  Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. 
  Return either pangram or not pangram as appropriate. 
  Complete the function pangrams in the editor below. 
  It should return the string pangram if the input string is a pangram. 
  Otherwise, it should return not pangram.
"""


def pangrams(s: str) -> str:
    """
    Determines if a string is a pangram or not.

    Args:
    s (str): The input string to be checked.

    Returns:
    str: 'pangram' if the string is a pangram, 'not pangram' otherwise.
    """
    
    # Define the set of all alphabets
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m',  
                'n','o','p','q', 'r','s','t','u','v','w', 'x','y', 'z'}
    
    # Initialize a variable to store the lowercase alphabetic characters from the input string
    store_letters = ''

    # Iterate through each character in the input string
    for letter in s:
        # Check if the character is an alphabet
        if letter.isalpha():
            # Convert the character to lowercase and add it to the store_letters string
            store_letters += letter.lower()

    # Convert the store_letters string to a set to remove duplicates
    store_letters = set(store_letters)

    # Find the difference between the alphabet set and the set of letters in the input string
    value = alphabet.difference(store_letters)

    # Check if the difference set is empty
    if not value:
        return 'pangram'
    else:
        return 'not pangram'
