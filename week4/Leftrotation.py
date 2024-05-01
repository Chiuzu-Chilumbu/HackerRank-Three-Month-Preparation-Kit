"""
Challenge: A left rotation operation on an array of size n shifts 
  each of the array's elements 1 unit to the left. Given an integer, d, 
  rotate the array that many steps left and return the result.

"""

def rotateLeft(d, arr):
    # Write your code here
    for _ in range(d):
        element = arr.pop(0)
        arr.append(element)
        
    return arr