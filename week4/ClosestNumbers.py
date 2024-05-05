"""
Challenge: Sorting is useful as the first step in many different tasks. 
  The most common task is to make finding things easier, but there are other uses as well. 
  In this case, it will make it easier to determine which pair or pairs of elements 
  have the smallest absolute difference between them.
"""

from typing import List, Tuple

def closestNumbers(arr: List[int]) -> List[int]:
    """
    Finds pairs of numbers in the input array that have the smallest absolute difference.

    Args:
    arr (List[int]): The input list of integers.

    Returns:
    List[int]: A list containing pairs of numbers with the smallest absolute difference.

    Notes:
    - The function first sorts the input array in ascending order.
    - It then iterates through adjacent pairs of numbers and calculates their absolute differences.
    - The pairs with the smallest absolute difference are stored in a dictionary.
    - Finally, the function retrieves the pairs with the smallest absolute difference and returns them as a list.
    """
    arr = sorted(arr)
    diff_store = {}

    # Iterate through adjacent pairs of numbers in the sorted array
    for index in range(len(arr) - 1):
        pair = arr[index], arr[index + 1]
        if pair not in diff_store:
            # Calculate and store the absolute difference between each pair of numbers
            diff_store[pair] = abs(pair[0] - pair[1])

    # Find the smallest absolute difference
    current_min = min(diff_store.values())
    pair_list = []

    # Iterate through the stored pairs to find those with the smallest absolute difference
    for pairs, diff in diff_store.items():
        if diff == current_min:
            pair_list.append(pairs[0])
            pair_list.append(pairs[1])

    return pair_list
