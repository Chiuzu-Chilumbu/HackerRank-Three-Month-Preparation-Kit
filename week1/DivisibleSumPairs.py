"""
challenge:  Given an array of integers and a positive integer,
  determine the number of  pairs where  and  +  is divisible by .
"""


def divisibleSumPairs(n, k, ar):
    """
    Determine the number of pairs (i, j) in array `ar` where i < j and (ar[i] + ar[j]) is divisible by k.

    Parameters:
    - n (int): The length of array `ar`.
    - k (int): The divisor.
    - ar (list of int): The list of integers.

    Returns:
    - int: The count of such pairs.
    """
    count = 0
    # Loop through each element in the list
    for i in range(n):
        # Second loop starts from the next element to avoid repeats and ensure
        # i < j
        for j in range(i + 1, n):
            # Check if the sum of the current pair is divisible by k
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count
