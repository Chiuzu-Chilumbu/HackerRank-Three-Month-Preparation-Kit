"""
Challenge: Two players are playing a game of Tower Breakers! 
  Player  always moves first, and both players always play optimally.The rules of the game are as follows:
  Initially there are n towers.
  Each tower is of height m.
  The players move in alternating turns.
  In each turn, a player can choose a tower of height  and reduce its height to y, where <= y < x and y evenly divides x.
  If the current player is unable to make a move, they lose the game.
  Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.
"""

def towerBreakers(n: int, m: int) -> int:
    """
    Determines the outcome of the Tower Breakers game given the dimensions of the grid.

    Args:
    n (int): The number of towers.
    m (int): The number of towers in each row.

    Returns:
    int: The number representing the winner of the Tower Breakers game, where:
         - 1 indicates the first player wins.
         - 2 indicates the second player wins.

    Notes:
    - If the number of towers is even or there is only one tower in each row, the second player wins.
    - Otherwise, the first player wins.
    """
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1
