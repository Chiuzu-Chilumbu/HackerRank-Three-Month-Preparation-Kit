"""
Challenge:
A smart number is defined as a number that has an odd number of divisors. Given several test cases, determine whether each number is a smart number or not. A number is smart if and only if it is a perfect square, as perfect squares have an odd number of divisors.

For each test case, the function should print "YES" if the number is a smart number, and "NO" otherwise.
"""

import math

def is_smart_number(num):
    """
    Args:
        num (int): The number to check if it is a smart number.

    Returns:
        bool: True if the number is a smart number (perfect square), otherwise False.
    """
    
    # Calculate the integer square root of the number
    val = int(math.sqrt(num))
    
    # Check if the square of the square root equals the number
    if val * val == num:
        return True
    return False

# Example usage:
for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
