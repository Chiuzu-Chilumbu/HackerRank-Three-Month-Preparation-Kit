"""
Challenge: 
"""


def pageCount(n, p):
    # Calculate the total number of page turns from the front
    forward_step_count = p // 2

    # Calculate the total number of page turns from the back
    if n % 2 == 0:
        n += 1  # This is to account for the extra page turn needed if `n` is even
    backward_step_count = (n - p) // 2

    # Return the minimum of the two counts
    return min(forward_step_count, backward_step_count)
