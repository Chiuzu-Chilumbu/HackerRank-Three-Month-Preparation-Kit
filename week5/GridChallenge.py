"""
Challenge:
You are given a grid of characters, where each row must be sorted lexicographically. After sorting the rows, check if each column is also sorted lexicographically. The task is to determine if the grid can be sorted in such a way that both rows and columns are sorted lexicographically.

"""

def gridChallenge(grid):
    """
    Args:
        grid (list): A list of strings representing the grid of characters.

    Returns:
        str: "YES" if the columns are also lexicographically sorted after sorting the rows; otherwise, "NO".
    """
    
    # Sort each row to make sure the rows are lexicographically sorted
    sorted_grid = [sorted(row) for row in grid]
    
    # Check columns for sorted order
    n = len(sorted_grid)
    for col in range(n):
        # Check if the current column is sorted
        if any(sorted_grid[row][col] > sorted_grid[row + 1][col] for row in range(n - 1)):
            return "NO"
    
    return "YES"

# Example usage:
grid = ['abc', 'ade', 'efg']
print(gridChallenge(grid))  # Output: YES
