"""
Challenge: A left rotation operation on an array of size n shifts 
  each of the array's elements 1 unit to the left. Given an integer, d, 
  rotate the array that many steps left and return the result.

"""
from typing import List

def rotateLeft(d: int, arr: List[int]) -> List[int]:
    """
    Rotates the elements of the input array to the left by the specified number of positions.

    Args:
    d (int): The number of positions to rotate the elements to the left.
    arr (List[int]): The input list of integers.

    Returns:
    List[int]: The rotated list of integers.

    Notes:
    - The function iterates 'd' times, each time removing the first element of the list and appending it to the end.
    - This effectively rotates the elements of the list to the left by 'd' positions.
    """
    for _ in range(d):
        # Remove the first element of the list and append it to the end
        element = arr.pop(0)
        arr.append(element)
        
    return arr
