"""
Challenge Description: Given five positive integers,
  find the minimum and maximum values that can be calculated by summing
  exactly four of the five integers. Then print the respective minimum and maximum
  values as a single line of two space-separated long integers.
"""


def miniMaxSum(arr: list) -> None:
    """
    Parameters:
    arr (list of int): The input array containing exactly five positive integers.

    Returns:
    None: This function prints the minimum and maximum sum separated by a space.

    Example usage:
    >>> arr = [1, 2, 3, 4, 5]
    >>> miniMaxSum(arr)
    10 14
    """

    #  obtain the smallest and largest element in the array
    smallest_element = min(arr)
    largest_element = max(arr)

    # obtain the total sum
    total_sum = sum(arr)

    # Find the maximum sum by subtracting the minimum value from the total sum.
    max_sum = total_sum - smallest_element
    # Find the minimum sum by subtracting the maximum value from the total sum.
    min_sum = total_sum - largest_element

    # Print the results.
    print(min_sum, max_sum)
