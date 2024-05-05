"""
Challenge : Julius Caesar protected his confidential information by encrypting it using a cipher. 
  Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, 
  just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
"""


def caesarCipher(s, k):
    # Write your code here
    cipher_text = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                letter_case = ord('A')
            else:
                letter_case = ord('a')
            
            # add the number of shifts to current letter
            new_index = ord(letter) + k 
            # ensure new index does not exceed z or 'Z' but shouldl restart
            new_index = (new_index - letter_case) % 26
            # convert the number back to letter
            cipher_letter = chr(new_index + letter_case)
            # add it to the cipher text
            cipher_text += cipher_letter
        else:
            cipher_text += letter
            
    return cipher_text