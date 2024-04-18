"""
Challenge : You will be given a list of 32 bit unsigned integers. 
  Flip all the bits ( and ) and return the result as an unsigned integer.
"""


def flippingBits(n: int) -> int:
    """
    Flips all the bits in a list of 32-bit unsigned integers and returns the result as an unsigned integer.

    Args:
    n : an unsigned integer to flip the bits for.

    Returns:
    int: The result after flipping the bits of the unsigned integer.
    """

    # Initialize a variable to store the result
    result = 0
    
    # 0xFFFFFFFF represents a 32-bit number where all bits are set to 1.
    thirty_two_bit_number = 0xFFFFFFFF
    
    # Flip the bits of the input integer 'n'
    flipped_num = n ^ thirty_two_bit_number
    
    # Mask the least significant 32 bits of the flipped number
    masked_flipped_num = flipped_num & 0xFFFFFFFF
    
    # Shift the masked flipped number to the left by 32 bits and combine it with the result
    result |= masked_flipped_num
    
    return result
