"""
Challenge : the task is to debug the existing code to successfully execute all provided test files.
  Given an array of n distinct integers, transform the array into a zig zag sequence 
  by permuting the array elements. A sequence will be called a zig zag sequence if the first k
  elements in the sequence are in increasing order 
  and the last k elements are in decreasing order, 

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.
To restore the original code, click on the icon to the right of the language selector.
original code : 

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
"""

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2) # changed from `int((n + 1)/2) to ensure the last 4 lines of the array are in decreasing order
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # changed from `ed = n - 1` to ensure the last number which is the smallest is not swapped it is already in correct position
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # changed from `ed = ed + 1` to ensure the end is decreasing not increasing

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return