"""
Challenge: Two players are playing a game of Tower Breakers!
"""

def towerBreakers(n, m):
    # Write your code here
    if n % 2 == 0 or m == 1:
        return 2
    
    else:
        return 1