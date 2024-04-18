"""
Challenge: A pangram is a string that contains every letter of the alphabet. 
  Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. 
  Return either pangram or not pangram as appropriate. 
  Complete the function pangrams in the editor below. 
  It should return the string pangram if the input string is a pangram. 
  Otherwise, it should return not pangram.
"""


def pangrams(s):
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m',  \
                'n','o','p','q', 'r','s','t','u','v','w', 'x','y', 'z'}
    
    store_letters = ''

    for letter in s:
        if letter.isalpha():
            store_letters += letter.lower()

    store_letters = set(store_letters)

    value = alphabet.difference(store_letters)

    if not value:
        return 'pangram'
    
    else:
        return 'not pangram'

