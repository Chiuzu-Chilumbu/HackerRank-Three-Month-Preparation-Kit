"""
Challenge: Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle
with the maximum possible perimeter. Return an array of the lengths of its sides as integers in increasing order.
If there are several valid triangles having the maximum perimeter: Choose the one with the longest maximum side.
If more than one has that maximum, choose from them the one with the longest minimum side.
If more than one has that maximum as well, print any one them.
If no non-degenerate triangle exists, return .
"""


def isValid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def maximumPerimeterTriangle(sticks):
    # If there are less than 3 sticks, it is not possible to form a triangle.
    if len(sticks) < 3:
        return [-1]

    # Sort the sticks in non-increasing order. This way, we try to form a triangle
    # with the longest sticks first, which helps us find the maximum perimeter.
    sticks.sort(reverse=True)

    # Iterate through the list of sticks, starting from the largest and
    # checking every triplet.
    for i in range(len(sticks) - 2):
        # We check if the current stick and the next two sticks can form a
        # triangle.
        if isValid_triangle(sticks[i], sticks[i + 1], sticks[i + 2]):
            # If they can form a triangle, we return the lengths in non-decreasing order.
            # This is accomplished simply by returning the sticks in the order we find them,
            # since the list is sorted in non-increasing order.
            return [sticks[i + 2], sticks[i + 1], sticks[i]]

    # If no valid triangle is found after checking all possible triplets,
    # return [-1].
    return [-1]
