"""
Challenge:
  
"""


def birthday(s, d, m):
    # Write your code here
	length = m 
	size = len(s)
	start = 0
	count = 0
	while length <= size:
		if sum(s[start:length]) == d:
			count += 1
		start += 1
		length += 1

	return count
    


s = [2, 2, 1, 3, 2]
d = 4
m = 2

print(birthday(s, d, m)) # 2