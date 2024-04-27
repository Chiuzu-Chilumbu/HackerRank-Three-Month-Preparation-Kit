"""
Challenge: Between Two sets

"""
from typing import List

def isMultiple(factor: int, arr: List[int]) -> bool:
    """
    Checks if a given factor is a multiple of all numbers in a list.

    Args:
    factor (int): The factor to check.
    arr (List[int]): The list of numbers to check against.

    Returns:
    bool: True if the factor is a multiple of all numbers in the list, False otherwise.
    """
    # Check if factor is a multiple of all numbers in arr
    return all(factor % number == 0 for number in arr)
    
def isDivisor(factor: int, arr: List[int]) -> bool:
    """
    Checks if a given factor is a divisor of all numbers in a list.

    Args:
    factor (int): The factor to check.
    arr (List[int]): The list of numbers to check against.

    Returns:
    bool: True if all numbers in the list are multiples of the factor, False otherwise.
    """
    # Check if all numbers in arr are multiples of factor
    return all(number % factor == 0 for number in arr)

def getTotalX(a: List[int], b: List[int]) -> int:
    """
    Calculates the total number of integers that are factors of the elements in list 'a' and divisors of the elements in list 'b'.

    Args:
    a (List[int]): The first list of integers.
    b (List[int]): The second list of integers.

    Returns:
    int: The total number of integers satisfying the conditions.

    Notes:
    - This function iterates through a range of numbers from the maximum value in 'a' to the minimum value in 'b'.
    - For each number in the range, it checks if it is a multiple of all elements in 'a' and a divisor of all elements in 'b'.
    - The counter is incremented for each number that satisfies both conditions.
    """
    # Obtain minimum and maximum values to compute range of factors
    _min = min(b)
    _max = max(a)
    counter = 0
    # Iterate to compute factors and check if they match the conditions
    for number in range(_max, _min + 1):
        if isMultiple(number, a) and isDivisor(number, b):
            counter += 1
            
    return counter
