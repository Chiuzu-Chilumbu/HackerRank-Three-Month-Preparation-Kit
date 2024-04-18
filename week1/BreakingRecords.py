"""
Challenge : Maria plays college basketball and wants to go pro.
  Each season she maintains a record of her play. She tabulates the number of times she breaks
  her season record for most points and least points in a game. Points scored in the first game
  establish her record for the season, and she begins counting from there.
"""


def breakingRecords(scores: list) -> list:
    """
    parameters:
scores (list of int): contains the score of maria throughout each season

returns:
list: A list of the times she broke maximum and minimum records in that order [max, min]

Example usage:
    arr = [10, 5, 20, 20, 4, 5, 2, 25, 1]
>>> breakingRecords(arr)
[2, 4]
    """
    # Declare variables that will be needed
# The current min and max score will be assigned to the first elements in
# the score board
    current_min_score = current_max_score = scores[0]
    max_record_break_count = min_record_break_count = 0

    # We loop through the current score starting from the second score and compare
# the first scores with the current score
    for current_score in scores[1:]:
        #  solve for breaking maximum record
        if current_score > current_max_score:
            current_max_score = current_score
            max_record_break_count += 1

        # we solve for breaking the minimum record
        elif current_score < current_min_score:
            current_min_score = current_score
            min_record_break_count += 1

        else:
            #  otherwise no record was broken
            continue

    return [max_record_break_count, min_record_break_count]