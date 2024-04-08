"""
Challenge Description: Given five positive integers,
  find the minimum and maximum values that can be calculated by summing
  exactly four of the five integers. Then print the respective minimum and maximum
  values as a single line of two space-separated long integers.
"""


def miniMaxSum(arr):
    """this function solves the minimaxsum problem"""
    smallest_element = min(arr)
    largest_element = max(arr)

    arr.remove(smallest_element)
    max_sum = sum(arr)

    arr.append(smallest_element)
    arr.remove(largest_element)

    min_sum = sum(arr)

    print(min_sum, max_sum)


# sample input:
arr_1 = [1, 3, 5, 7, 9]

"""
sample output:
16 24
"""

#  sample input:
arr_2 = [1, 2, 3, 4, 5]

"""
sample output:
10 14
"""

# sample input:
arr_3 = [7, 69, 2, 221, 8974]

"""
sample output:
299 9271
"""
