"""
Challenge: Given an array of integers,
where all elements but one occur twice, find the unique element.
"""


def lonelyinteger(a):
    """
    Complete the lonelyinteger function in the editor below.
	lonelyinteger has the following parameter(s):
	int a[n]: an array of integers
	Returns
	int: the element that occurs only once
	"""

    dict_counter = {}

    for element in a:
        if element not in dict_counter:
            dict_counter[element] = 1

        else:
            dict_counter[element] += 1

    for element, value in dict_counter.items():
        if value == 1:
            return element



arr = [1, 2, 3, 4, 3, 2, 1]
print(lonelyinteger(arr))