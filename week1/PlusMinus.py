"""
Challenge Description: Given an array of integers,
calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.
"""


def plusMinus(arr: list) -> None:
    """
    Parameters:
    arr (list of int): The input array containing negative, positive and zero value integers.

    Returns:
    None: This function prints the proportion of the negative, positive and zero values in new lines.

    Example usage:
    >>> arr = [1, 1, 0, -1, -1]
    >>> plusMinus(arr)

    0.400000
    0.400000
    0.200000
    """

    # assign positives, negatives, zeros to 0
    positives, negatives, zeros = 0, 0, 0
    #  obtain the length of the array
    length_of_arr = len(arr)

    # loop through the elements in the array and how many instances of
    # positives, negatives, zeros are present in the array
    for element in arr:
        if element > 0:
            positives += 1

        elif element < 0:
            negatives += 1

        else:
            zeros += 1

    # Calculate the proportion of the collected instances positives,
    # negatives, zeros
    positives = positives / length_of_arr
    negatives = negatives / length_of_arr
    zeros = zeros / length_of_arr

    # print the calculated proportions to 6 decimal places
    print(f"{positives:6f}")
    print(f"{negatives:6f}")
    print(f"{zeros:6f}")
