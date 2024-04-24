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

# Debugged Code Solution:

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]: # Corrected from assign to equals
            res += '0'  # have to add to the result not assign and remove semi colon
        else:
            res += '1' # have to add to the result not assign and remove semi colon

    return res

s = input()
t = input()
print(strings_xor(s, t))


