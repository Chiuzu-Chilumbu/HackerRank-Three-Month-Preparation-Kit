"""
challenge : Given a square matrix, 
calculate the absolute difference between the sums of its diagonals.
"""

from typing import List

def diagonalDifference(arr: List[List[int]]) -> int:
    # Write your code here
    matrix_size = len(arr[0])
    right_to_left = 0
    left_to_right = 0
    
    for i in range(matrix_size):
        right_to_left += arr[i][i]
    

    for i in range(matrix_size):
        left_to_right += arr[i][matrix_size - 1 - i]
                
    result = abs(right_to_left - left_to_right)
    return result



arr_1 =  [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
arr_2 = [[1, 2, 3,], [4, 5, 6], [9, 8, 9]] 


print(diagonalDifference(arr_1))