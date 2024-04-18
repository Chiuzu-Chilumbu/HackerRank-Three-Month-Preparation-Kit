"""
Challenge: An avid hiker keeps meticulous records of their hikes. 
  During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , 
  or a downhill, step. Hikes always start and end at sea level, and each step up or down 
  represents a unit change in altitude. We define the following terms: 
  A mountain is a sequence of consecutive steps above sea level, 
  starting with a step up from sea level and ending with a step down to sea level.
  A valley is a sequence of consecutive steps below sea level, 
  starting with a step down from sea level and ending with a step up to sea level. 
  Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
"""


def countingValleys(steps :int, path: str) -> int:
    """
    Counts the number of valleys traversed in the path sequence.

    Args:
    steps (int): The total number of steps in the path.
    path (str): A string representing the sequence of steps taken, where 'U' denotes an upward step and 'D' denotes a downward step.

    Returns:
    int: The number of valleys traversed in the path.
    """

    # Define symbols for upward and downward steps
    up = 'U'
    down = 'D'
    
    # Initialize variables for sea level and valley count
    sea_level = 0
    valley_count = 0
    
    # Iterate through each step in the path
    for step in range(steps):
        # Increment sea level for upward steps, decrement for downward steps
        if path[step] == up:
            sea_level += 1
        elif path[step] == down:
            sea_level -= 1
        
        # Check if a valley is completed (sea level returns to 0 after descending)
        if sea_level == 0 and path[step] == up:
            valley_count += 1
            
    return valley_count
