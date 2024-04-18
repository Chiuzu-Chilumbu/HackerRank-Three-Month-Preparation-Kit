"""
challenge : Given a square matrix, 
calculate the absolute difference between the sums of its diagonals.
"""


from typing import List

def diagonalDifference(arr: List[List[int]]) -> int:
    """
    Calculates the absolute difference between the sums of the main diagonal and secondary diagonal of a square matrix.

    Args:
    arr (List[List[int]]): The square matrix represented as a list of lists.

    Returns:
    int: The absolute difference between the sums of the main diagonal and secondary diagonal.
    """

    # Initialize variables to store the sums of diagonals
    right_to_left = 0
    left_to_right = 0
    
    # Get the size of the square matrix
    size = len(arr)
    
    # Iterate through each row of the matrix
    for i in range(size):
        # Add elements from the main diagonal (top-left to bottom-right)
        right_to_left += arr[i][i]
        # Add elements from the secondary diagonal (top-right to bottom-left)
        left_to_right += arr[i][size - 1 - i]

    # Calculate the absolute difference between the sums of diagonals
    result = abs(right_to_left - left_to_right)

    return result
