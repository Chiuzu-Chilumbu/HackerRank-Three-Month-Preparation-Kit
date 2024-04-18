"""
Challenge: Given a list of integers,
count and return the number of times each value appears as an array of integers.
"""

from typing import List

def countingSort(arr: List[int]):
    """
    Counts the occurrences of each integer value in the input list and returns an array of counts.

    Args:
    arr (list): The list of integers to be processed.

    Returns:
    list: An array of integers representing the count of occurrences for each value in the input list.
    """

    # Initialize an array to store the counts of each integer value
    result_arr = [0 for _ in range(100)]

    # Create a set of unique elements in the input list to avoid redundant counting
    element_set = set(arr)

    # Iterate through the unique elements and count their occurrences in the input list
    for element in element_set:
        # Initialize count for the current element
        count = 0
        # Count the occurrences of the current element in the input list
        count = arr.count(element)
        # Update the count in the result array at the index corresponding to the current element
        result_arr[element] = count

    return result_arr


