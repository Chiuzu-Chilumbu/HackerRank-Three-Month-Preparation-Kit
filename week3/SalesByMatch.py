"""
Challenge : There is a large pile of socks that must be paired by color.
  Given an array of integers representing the color of each sock,
  determine how many pairs of socks with matching colors there are.

"""


def sockMerchant(n: int, ar: list) -> int:
    """
    Counts the number of pairs of socks with matching colors.

    Args:
    n (int): The number of socks in the pile.
    ar (list): A list representing the colors of the socks.

    Returns:
    int: The number of pairs of socks with matching colors.
    """

    pair_count = 0
    set_store = set()
    # iterates through the list of socks
    for element in ar:
        # keeps track of unique colors using a set
        # Whenever a sock with a color already in the set is encountered,
        # it is considered a pair and removed from the set otherwise it is
        # added
        if element not in set_store:
            set_store.add(element)
        else:
            set_store.remove(element)
            # The count of pairs is incremented for each matching color
            # encountered.
            pair_count += 1

    return pair_count
