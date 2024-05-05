"""
Challenge: 
"""

def closestNumbers(arr):
    # Write your code here
    arr = sorted(arr)
    diff_store = {}
    
    for index in range(len(arr) - 1):
        pair = arr[index], arr[index+1]
        if pair not in diff_store:
            diff_store[pair] = abs(pair[0] - pair[1])
            
    
    current_min = min(diff_store.values())
    pair_list = []
    
    for pairs, diff in diff_store.items():
        if diff == current_min:
            pair_list.append(pairs[0])
            pair_list.append(pairs[1])
            
    return pair_list
        