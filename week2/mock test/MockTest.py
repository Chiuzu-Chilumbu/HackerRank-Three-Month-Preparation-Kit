"""
Challenge: Flipping Matrix
"""

def flippingMatrix(matrix):
    """
    Calculates the maximum sum of elements in the upper-left quadrant after flipping certain elements of the matrix.

    Args:
    matrix (list of lists): The input square matrix.

    Returns:
    int: The maximum sum of elements in the upper-left quadrant.

    Raises:
    ValueError: If the input matrix is not square.
    """
    max_total = 0
    
    # Determine the size of the upper-left quadrant
    n = len(matrix) // 2  
    
    # Iterate through the upper-left quadrant
    for i in range(n):
        for j in range(n):
            # Calculate the indices for accessing elements in other quadrants
            upper_right_i = i
            upper_right_j = len(matrix) - j - 1
            lower_left_i = len(matrix) - i - 1
            lower_left_j = j
            lower_right_i = len(matrix) - i - 1
            lower_right_j = len(matrix) - j - 1
            
            # Find the maximum element among the four
            max_s = max(matrix[i][j], matrix[upper_right_i][upper_right_j], 
                        matrix[lower_left_i][lower_left_j], matrix[lower_right_i][lower_right_j])
            
            # Add the maximum element to the total sum
            max_total += max_s
    
    return max_total
