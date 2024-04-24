"""
Challenge 
"""

def sockMerchant(n, ar):
    # Write your code here
    pair_count = 0
    set_store = set()
    for element in ar:
        if element not in set_store:
            set_store.add(element)
            
        elif element in set_store:
            set_store.remove(element)
            pair_count += 1
            
    return pair_count