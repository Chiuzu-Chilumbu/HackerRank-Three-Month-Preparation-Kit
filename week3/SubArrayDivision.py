"""
Challenge: Two children, Lily and Ron, want to share a chocolate bar. 
Each of the squares has an integer on it. Lily decides to share a contiguous segment of the bar selected such that:
The length of the segment matches Ron's birth month, and, The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.
  
"""


def birthday(s: list, d: int, m: int) -> int:
    """
    Counts the number of contiguous subarrays of chocolate squares with a given sum and length.

    Args:
    s (list): A list representing the chocolate squares.
    d (int): The desired sum of the contiguous subarray.
    m (int): The desired length of the contiguous subarray.

    Returns:
    int: The number of contiguous subarrays with the specified sum and length.
    """

    # Declare variables
    length = m
    size = len(s)
    start = 0
    count = 0

    # iterate through all possible contiguous subarrays of length `m` in the input list `s`
    while length <= size:
        # If the sum matches `d`, the count is incremented
        if sum(s[start:length]) == d:
            count += 1
        start += 1
        length += 1

    return count
