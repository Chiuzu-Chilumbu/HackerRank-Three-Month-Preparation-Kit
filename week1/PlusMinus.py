"""
Challenge Description: Given an array of integers,
calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.
"""


def plusMinus(arr):
    """this function solves the plus minus problem"""
    positives, negatives, zeros = 0, 0, 0
    size_of_arr = len(arr)

    for element in arr:
        if element > 0:
            positives += 1

        elif element < 0:
            negatives += 1

        else:
            zeros += 1

    positives = positives / size_of_arr
    negatives = negatives / size_of_arr
    zeros = zeros / size_of_arr

    print(f"{positives:6f}")
    print(f"{negatives:6f}")
    print(f"{zeros:6f}")


# sample input:
arr_1 = [1, 1, 0, -1, -1]

"""
sample output:
0.400000
0.400000
0.200000
"""

# Sample input:
arr_2 = [-4, 3, -9, 0, 4, 1]

"""
sample output:
0.500000
0.333333
0.166667
"""

