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
