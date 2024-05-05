"""
Challenge : Anagrams
"""


def anagram(s):
    # Write your code here
    size = len(s)

    if size % 2 != 0:
        return -1

    mid = size // 2
    string_1, string_2 = s[:mid], s[mid:]

    freq_1 = {}
    freq_2 = {}

    for char in string_1:
        if char in freq_1:
            freq_1[char] += 1
        else:
            freq_1[char] = 1

    for char in string_2:
        if char in freq_2:
            freq_2[char] += 1
        else:
            freq_2[char] = 1

    changes = 0
    for char in set(freq_1.keys()).union(set(freq_2.keys())):
        c1 = freq_1.get(char, 0)
        c2 = freq_2.get(char, 0)
        changes += abs(c1 - c2)

    return changes // 2
