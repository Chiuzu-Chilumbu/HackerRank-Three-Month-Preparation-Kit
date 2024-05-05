"""
challenge: You are choreographing a circus show with various animals. For one act, 
  you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
  The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
  The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
  You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

"""

def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    """
    Determines if two kangaroos will meet at the same location after a number of jumps.

    Args:
    x1 (int): The starting position of the first kangaroo.
    v1 (int): The jump distance of the first kangaroo.
    x2 (int): The starting position of the second kangaroo.
    v2 (int): The jump distance of the second kangaroo.

    Returns:
    str: 'YES' if the kangaroos will meet at the same location, 'NO' otherwise.

    Notes:
    - If the jump distances of both kangaroos are equal, they will only meet if they are initially at the same position.
    - Otherwise, if the relative jump speed (difference in starting positions divided by difference in jump distances) 
      is a non-negative integer, the kangaroos will meet.
    """
    if v1 == v2:
        # If both kangaroos have the same jump distance, they will meet only if they start at the same position
        if x1 == x2:
            return 'YES'
        else:
            return 'NO'
    else:
        # Calculate if they will meet using the relative jump speed
        if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0:
            return 'YES'
        else:
            return 'NO'
