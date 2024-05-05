"""
Challenge: Perform q queries where each query consists of some integer string s. 
  For each query, print whether or not the string is beautiful on a new line. 
  If it is beautiful, print YES x, where  is the first number of the increasing sequence. 
  If there are multiple such values of x, choose the smallest. Otherwise, print NO.
"""

def separateNumbers(s: str) -> None:
    """
    Checks if the string can be split into a sequence of beautiful numbers.

    Args:
    s (str): The input string.

    Returns:
    None: Prints "YES" followed by the first number in the sequence if it can be split into a sequence of beautiful numbers, otherwise prints "NO".

    Notes:
    - The function iterates through different lengths for the first number in the beautiful sequence.
    - It then generates the rest of the sequence and checks if the entire string is correctly segmented.
    """
    # Edge case for single character strings or leading zero
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    # Try different lengths for the first number in the beautiful sequence
    for length in range(1, len(s)):
        first_number = int(s[:length])
        current_number = first_number
        index = length
        flag = True

        # Generate the rest of the sequence
        while index < len(s):
            next_number = current_number + 1
            next_number_str = str(next_number)
            next_number_length = len(next_number_str)

            # Check if the next number can be a flag prefix
            if s[index:index + next_number_length] == next_number_str:
                index += next_number_length
                current_number = next_number
            else:
                flag = False
                break

        # If the entire string is correctly segmented
        if flag and index == len(s):
            print(f"YES {first_number}")
            return

    # If no flag sequence found
    print("NO")
