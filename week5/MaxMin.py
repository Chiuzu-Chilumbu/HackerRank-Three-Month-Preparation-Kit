"""
Challenge:
You will be given a list of integers, arr, and a single integer k. 
You must create an array of length k from elements of arr such that its unfairness is minimized. 
Call that array arr'. Unfairness of an array is calculated as:

max(arr') - min(arr')

Where:
- max denotes the largest integer in arr'
- min denotes the smallest integer in arr'
""" 


def maxMin(k, arr):
    """
    Calculates the minimum possible unfairness for a subarray of length 'k' chosen from 'arr'.

    Args:
        k (int): The number of elements to select for the subarray.
        arr (list): The array of integers from which to choose the subarray.

    Returns:
        int: The minimum possible unfairness among all subarrays of length 'k'.
         
    """

    # Sort the array 
    arr.sort()

    # Initialize minimum unfairness to a large value
    min_unfairness = float('inf')

    # Iterate through the array and find the minimum unfairness
    for i in range(len(arr) - k + 1):
        # Calculate the unfairness of the subarray from index i to i+k-1
        current_unfairness = arr[i + k - 1] - arr[i]

        # Update the minimum unfairness if the current one is smaller
        if current_unfairness < min_unfairness:
            min_unfairness = current_unfairness

    return min_unfairness