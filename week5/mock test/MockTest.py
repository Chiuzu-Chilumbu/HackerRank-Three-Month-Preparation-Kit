"""
Challenge:
Implement a modified Fibonacci sequence using the following definition:
Given terms t1 and t2, where i ∈ (1, ∞), term t[i+2] is computed as:
t[i+2] = t[i] + (t[i+1])^2
Given three integers, t1, t2, and n, compute and print the nth term of a modified Fibonacci sequence.

"""

def fibonacciModified(t1, t2, n):
    """
    Args:
    t1 (int): The first term of the Fibonacci sequence.
    t2 (int): The second term of the Fibonacci sequence.
    n (int): The nth position in the sequence to compute.

    Returns:
        int: The nth term in the modified Fibonacci sequence.

    """
    # Convert inputs to integers in case they're passed as strings
    t1, t2, n = int(t1), int(t2), int(n)
    
    # Handle the base cases directly
    if n == 1:
        return t1
    elif n == 2:
        return t2

    # Initialize the first two terms
    prev, current = t1, t2

    # Compute each term up to the nth term
    for _ in range(3, n + 1):
        # The next term is the sum of the previous term and the square of the current term
        next_term = prev + current ** 2
        prev, current = current, next_term

    # Return the nth term of the modified Fibonacci sequence
    return current

# Example usage
print(fibonacciModified(0, 1, 6))  # Expected output: 27
