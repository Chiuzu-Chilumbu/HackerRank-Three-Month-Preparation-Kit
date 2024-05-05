"""
Challenge : Julius Caesar protected his confidential information by encrypting it using a cipher. 
  Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, 
  just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
"""


def caesarCipher(s: str, k: int) -> str:
    """
    Encrypts the input string using the Caesar cipher with the given key.

    Args:
    s (str): The input string to be encrypted.
    k (int): The key for the Caesar cipher.

    Returns:
    str: The encrypted string.

    Notes:
    - For each letter in the input string, the function shifts the letter by 'k' positions in the alphabet.
    - If the character is a letter, it determines the case (uppercase or lowercase) and applies the shift accordingly.
    - Non-alphabetic characters remain unchanged in the encrypted string.
    """
    cipher_text = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                letter_case = ord('A')
            else:
                letter_case = ord('a')
            
            # Add the number of shifts to the current letter's ASCII value
            new_index = ord(letter) + k 
            # Ensure the new index does not exceed 'Z' or 'z', wrapping around if necessary
            new_index = (new_index - letter_case) % 26
            # Convert the ASCII value back to a letter
            cipher_letter = chr(new_index + letter_case)
            # Add the encrypted letter to the cipher text
            cipher_text += cipher_letter
        else:
            # Non-alphabetic characters remain unchanged
            cipher_text += letter
            
    return cipher_text
