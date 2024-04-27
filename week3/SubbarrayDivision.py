"""
Challenge:
  
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

    Notes:
    - This function iterates through all possible contiguous subarrays of length `m` in the input list `s`.
    - For each subarray, it calculates the sum and compares it with the desired sum `d`.
    - If the sum matches `d`, the count is incremented.
    """
    length = m
    size = len(s)
    start = 0
    count = 0
    while length <= size:
        if sum(s[start:length]) == d:
            count += 1
        start += 1
        length += 1

    return count
