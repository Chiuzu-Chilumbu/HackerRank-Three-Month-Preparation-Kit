"""
Challenge:
  Camel Case is a naming style common in many programming languages.
  In Java, method and variable names typically start with a lowercase letter,
  with all subsequent words starting with a capital letter (example: startThread).
  Names of classes follow the same pattern, except that they start with a capital letter.
  Task is to write a program that creates or splits Camel Case variable, method, and class names.
"""

import sys

def split_helper(word):
    """
    Splits a CamelCase string into a space-delimited string with all lowercase letters.

    Args:
    word (str): The CamelCase string to split.

    Returns:
    str: A string of words separated by spaces, all in lowercase, stripped of any parentheses.
    
    This function iterates through each character in the input string. When it encounters an uppercase letter
    or a parenthesis, it treats this as the start of a new word, appending the current word to the list and
    resetting for the next word. It ensures that characters like parentheses are not included in the output.
    """
    words_list = []
    current_word = word[0]

    for letter in word[1:]:
        if letter.isupper():
            words_list.append(current_word.lower())
            current_word = letter.lower()
        else:
            current_word += letter

    if current_word:
        words_list.append(current_word.strip('()'))

    return ' '.join(words_list)



def merge_helper(word, method):
    """
    Merges a space-delimited string into a CamelCase string based on the specified method type.

    Args:
    word (str): The space-delimited string to convert into CamelCase.
    method (str): The type of CamelCase format ('M' for methods, 'C' for classes, 'V' for variables).

    Returns:
    str: A CamelCase string formatted according to the method type. Methods end with '()', classes start with
    an uppercase letter, and variables follow camelCase convention without additional characters.
    
    The function handles three cases:
    - 'M': Starts with a lowercase letter, subsequent words start with uppercase, ends with '()'
    - 'C': Each word starts with an uppercase letter
    - 'V': Starts with a lowercase letter, subsequent words start with uppercase
    """
    word_list = word.split(' ')

    if method == 'M':
        camel_case_word_list = []

        for index, word in enumerate(word_list):
            if index == 0:
                camel_case_word_list.append(word)

            else:
                camel_case_word_list.append(word.capitalize())

        return ''.join(camel_case_word_list) + '()'

    elif method == 'C':
        return ''.join(word.capitalize() for word in word_list)

    else:
        camel_case_word_list = []
        for index, word in enumerate(word_list):
            if index == 0:
                camel_case_word_list.append(word)

            else:
                camel_case_word_list.append(word.capitalize())

        return ''.join(camel_case_word_list)


def camel_case():
    """
    Processes multiple lines of input, each specifying an operation ('S' for split or 'C' for combine),
    a method type ('M', 'C', 'V'), and the word to operate on. Outputs the result of the operation.

    This function reads from standard input until EOF. For each line, it determines whether to split
    or merge the provided word based on the operation and method type. The results are printed directly.
    """

    input = sys.stdin.read
    data = input().splitlines()

    for string in data:
        parts = string.split(';')
        operation = parts[0]
        method = parts[1]
        word = parts[2]

        if operation == 'S':
            print(split_helper(word))

        else:
            print(merge_helper(word, method))