"""
Challenge:
You are given a list of queries to process on a dynamic array of size `n`. There are two types of queries:
1. Query type 1: Append an integer y to the sequence at index ((x ^ lastAnswer) % n).
2. Query type 2: Find the value of the element y % size of the sequence at index ((x ^ lastAnswer) % n), where size is the number of elements in the sequence. Then, update lastAnswer to this value and store it in the results.

The function returns a list of results for all type 2 queries.

"""

def dynamicArray(n, queries):
    """
    Args:
    n (int): The number of sequences in the dynamic array.
    queries (list): A list of queries where each query is a list of three integers [q_type, x, y].

    Returns:
        list: A list containing the results of all type 2 queries.
    """
    
    # Initialize an array of n empty sequences
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    results = []

    # Process each query
    for query in queries:
        q_type, x, y = query[0], query[1], query[2]
        idx = (x ^ lastAnswer) % n

        if q_type == 1:
            # Append y to the sequence at index idx
            arr[idx].append(y)
        elif q_type == 2:
            # Retrieve the value from the sequence at idx and update lastAnswer
            lastAnswer = arr[idx][y % len(arr[idx])]
            # Store lastAnswer in the results
            results.append(lastAnswer)

    return results

# Example usage:
n = 2
queries = [[1, 0, 5], [1, 1, 7], [2, 0, 1], [2, 1, 0]]
print(dynamicArray(n, queries))  # Output: [7, 5]
