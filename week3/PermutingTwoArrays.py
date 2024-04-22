"""
Challenge: In the problem you're working on, determine if there exists a permutation 
for each of the arrays A and B  such that when each element from array A' is added 
to each corresponding element from array B', all the results are greater than or equal to `k`.

Note : 
 
key to solving this problem is to realize that you don't have to actually generate the permutations. 
You just need to ensure that for each element `a` in A, there exists an element `b` in B 
such that `a + b` is greater than or equal to `k`.

To ensure this, you can sort one array in ascending order and the other in descending order.
By doing this, you pair the smallest elements of one array with the largest elements of the other, 
maximizing the chances that their sum will be at least `k`.

"""

def twoArrays(k, A, B):
    # Write your code here
    flag = True
    size = len(A)
    
    new_A = sorted(A, reverse=True)
    new_B = sorted(B)
    
    for index in range(size):
        if new_A[index] + new_B[index] < k:
            flag = False
            break
            
    if flag:
        return 'YES'
        
    else:
        return 'NO'