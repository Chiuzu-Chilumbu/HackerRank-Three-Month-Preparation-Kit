"""
Challenge: Given an array of integers,
where all elements but one occur twice, find the unique element.
"""

from typing import List

def lonelyinteger(a: List[int]) -> int:
    """
    Finds and returns the element that occurs only once in the given array of integers.

    Args:
    a (list): An array of integers.

    Returns:
    int: The element that occurs only once.
    """
    
    # Initialize a dictionary to count occurrences of each element
    dict_counter = {}

    # Iterate through the array and update the counts in the dictionary
    for element in a:
        if element not in dict_counter:
            dict_counter[element] = 1
        else:
            dict_counter[element] += 1

    # Iterate through the dictionary items to find the element that occurs only once
    for element, value in dict_counter.items():
        if value == 1:
            return element

