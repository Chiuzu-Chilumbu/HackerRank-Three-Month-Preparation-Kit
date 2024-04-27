"""
challenge: the task is to debug the existing code to successfully execute all provided test files.
  Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
  To know more about XOR Click Here

  Debug the given function strings_xor to find the XOR of the two given strings appropriately.
  Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.


Original Code :

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] = t[i]:
            res = '0';
        else:
            res = '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))

"""

#  Debugged Code Solution:


def strings_xor(s: str, t: str) -> str:
    """
    Finds the XOR of two strings consisting of digits 0 and 1 only.

    Args:
    s (str): The first input string.
    t (str): The second input string.

    Returns:
    str: The XOR of the two input strings.

    Notes:
    - The XOR operation is applied character by character between the two strings.
    - Modifies the input list in place to create the zigzag sequence.
    """

    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:  # Corrected from assignment to equality operation
            res += '0'    # Adds '0' to the result string if the corresponding characters are equal
        else:
            res += '1'    # Adds '1' to the result string if the corresponding characters are different

    return res
