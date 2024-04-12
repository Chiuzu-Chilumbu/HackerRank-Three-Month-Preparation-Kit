"""
Challenge:  Find the median
"""


def findMedian(arr: list):
    """
    The function is expected to return an INTEGER.
    The function accepts INTEGER_ARRAY arr as parameter.
    """
    arr_sorted = sorted(arr)

    middle = len(arr) // 2
    
    return arr_sorted[middle]
