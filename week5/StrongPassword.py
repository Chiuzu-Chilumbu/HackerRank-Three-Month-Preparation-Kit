"""
Challenge:
    Given a password string that Louise typed, the function calculates the minimum number of characters she must add to make her password strong.
    A strong password meets the following criteria:
    - Its length is at least 6 characters.
    - It contains at least one digit.
    - It contains at least one lowercase English character.
    - It contains at least one uppercase English character.
    - It contains at least one special character from the set: !@#$%^&*()-+
"""

def minimumNumber(n, password):
    """
    Args:
        n (int): The length of the password string Louise typed.
        password (str): The password string Louise typed.

    Returns:
        int: The minimum number of characters needed to add to make the password meet all the strong criteria.
    """

    # Define the sets of required characters
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # Flags to check the presence of each character type
    has_number = any(char in numbers for char in password)
    has_lower = any(char in lower_case for char in password)
    has_upper = any(char in upper_case for char in password)
    has_special = any(char in special_characters for char in password)

    # Count the number of missing character types
    missing_types = 4 - sum([has_number, has_lower, has_upper, has_special])

    # Calculate the number of characters to add to meet the minimum length requirement
    if n < 6:
        return max(missing_types, 6 - n)
    else:
        return missing_types