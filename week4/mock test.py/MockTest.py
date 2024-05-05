"""
Challenge : Anagrams
"""

def anagram(s: str) -> int:
    """
    Calculates the minimum number of changes required to make two halves of a string anagrams of each other.

    Args:
    s (str): The input string.

    Returns:
    int: The minimum number of changes required to make the two halves anagrams, or -1 if the length of the string is odd.

    Notes:
    - If the length of the string is odd, it's impossible to split it into two equal halves, so the function returns -1.
    - Otherwise, it splits the string into two halves and calculates the frequency of each character in both halves.
    - Then, it iterates through the unique characters in both halves, calculating the difference in frequencies and accumulating the changes required.
    - Finally, it returns half of the accumulated changes, as each change contributes to making both halves anagrams.
    """
    size = len(s)

    if size % 2 != 0:
        return -1

    mid = size // 2
    string_1, string_2 = s[:mid], s[mid:]

    freq_1 = {}
    freq_2 = {}

    # Calculate the frequency of characters in the first half of the string
    for char in string_1:
        if char in freq_1:
            freq_1[char] += 1
        else:
            freq_1[char] = 1

    # Calculate the frequency of characters in the second half of the string
    for char in string_2:
        if char in freq_2:
            freq_2[char] += 1
        else:
            freq_2[char] = 1

    changes = 0
    # Iterate through the union of characters in both halves
    for char in set(freq_1.keys()).union(set(freq_2.keys())):
        c1 = freq_1.get(char, 0)
        c2 = freq_2.get(char, 0)
        # Accumulate the absolute difference in frequencies
        changes += abs(c1 - c2)

    # Return half of the accumulated changes
    return changes // 2
