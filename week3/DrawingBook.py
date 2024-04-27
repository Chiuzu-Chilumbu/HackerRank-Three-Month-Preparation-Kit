"""
Challenge: A teacher asks the class to open their books to a page number.
A student can either start turning pages from the front of the book or from the back of the book.
They always turn pages one at a time. When they open the book, page 1 is always on the right side:
"""


def pageCount(n: int, p: int) -> int:
    """
    Calculates the minimum number of page turns needed to reach a specific page.

    Args:
    n (int): The total number of pages in the book.
    p (int): The page number to reach.

    Returns:
    int: The minimum number of page turns needed to reach the specified page.
    """
    # Calculate the total number of page turns from the front
    forward_step_count = p // 2

    # Calculate the total number of page turns from the back
    if n % 2 == 0:
        n += 1  # This is to account for the extra page turn needed if `n` is even
    backward_step_count = (n - p) // 2

    # Return the minimum of the two counts
    return min(forward_step_count, backward_step_count)
