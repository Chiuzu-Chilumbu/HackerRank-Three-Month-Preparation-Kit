"""
Challenge: Given a list of integers, 
count and return the number of times each value appears as an array of integers.
"""

def countingSort(arr):
    # Write your code here
    result_arr = [0 for _ in range(100)]
    element_set = set(arr)
    
    for element in element_set:
        count = 0
        count = arr.count(element)
        result_arr[element] = count
    
    return result_arr
arr = [1, 1, 3, 2, 1]

print(countingSort(arr))