"""
Challenge: Complete the minimumAbsoluteDifference function in the editor below. 
It should return an integer that represents the minimum absolute difference 
between any pair of elements. minimumAbsoluteDifference has the following parameter(s):

I found that both solutions work for this problem, i'm not sure is solution 2 is the best but it works
"""

# solution 1
def minimumAbsoluteDifference(arr):
    # Write your code here
    arr = sorted(arr)
    current_min = float('inf')
    
    for index in range(len(arr) - 1):
        print(arr[index])
        current_min = min(current_min, abs(arr[index] - arr[index+1]))
    
    return current_min


# solution 2
def minimumAbsoluteDifference(arr):
    # Write your code here
    arr = sorted(arr)
    current_min = float('inf')
    
    for index in range(len(arr)):
        current_min = min(current_min, abs(arr[index] - arr[index-1]))
    
    return current_min
