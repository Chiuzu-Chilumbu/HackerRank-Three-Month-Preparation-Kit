"""
Challenge:  Find the median
"""


def findMedian(arr: list):
    """
    Calculates the median value of the given list of integers.

    Args:
    arr (list of int): The input list of integers.

    Returns:
    int: The median value of the input list.

    Raises:
    TypeError: If the input argument is not a list.
    """
    # Sort the input list in ascending order
    arr_sorted = sorted(arr)

    # Calculate the index of the middle element
    middle = len(arr) // 2
    
    # Return the middle element as the median
    return arr_sorted[middle]
