"""
Challenge: Complete the minimumAbsoluteDifference function in the editor below. 
It should return an integer that represents the minimum absolute difference 
between any pair of elements. minimumAbsoluteDifference has the following parameter(s):

I found that both solutions work for this problem, i'm not sure is solution 2 is the best but it works
"""


from typing import List

# Solution 1
def minimumAbsoluteDifference_solution1(arr: List[int]) -> int:
    """
    Finds the minimum absolute difference between any pair of elements in the input array.

    Args:
    arr (List[int]): The input list of integers.

    Returns:
    int: The minimum absolute difference between any pair of elements.

    Notes:
    - The function first sorts the input array in ascending order.
    - It then iterates through adjacent pairs of numbers and calculates their absolute differences.
    - The minimum absolute difference found during iteration is returned.
    """
    arr = sorted(arr)
    current_min = float('inf')
    
    for index in range(len(arr) - 1):
        current_min = min(current_min, abs(arr[index] - arr[index + 1]))
    
    return current_min


# Solution 2
def minimumAbsoluteDifference_solution2(arr: List[int]) -> int:
    """
    Finds the minimum absolute difference between any pair of elements in the input array.

    Args:
    arr (List[int]): The input list of integers.

    Returns:
    int: The minimum absolute difference between any pair of elements.

    Notes:
    - The function first sorts the input array in ascending order.
    - It then iterates through the array and calculates the absolute differences between each element and its previous element.
    - The minimum absolute difference found during iteration is returned.
    """
    arr = sorted(arr)
    current_min = float('inf')
    
    for index in range(len(arr)):
        current_min = min(current_min, abs(arr[index] - arr[index - 1]))
    
    return current_min
