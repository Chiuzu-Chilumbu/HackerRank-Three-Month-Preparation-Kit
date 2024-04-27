"""
Challenge:  Given an array of bird sightings where every element represents a bird type id,
determine the id of the most frequently sighted type. If more than 1 type has been spotted
that maximum amount, return the smallest of their ids.
"""

from collections import Counter


def migratoryBirds(arr: list) -> int:
    """
    Finds the type of bird with the most sightings and the lowest ID number.

    Args:
    arr (list): A list of integers representing the types of birds sighted.

    Returns:
    int: The type of bird with the most sightings and the lowest ID number.
    """

    # use the Counter class from the collections module to count the
    # occurrences of each bird type
    counts = Counter(arr)

    # finds the maximum frequency of bird sightings.
    max_frequency = max(counts.values())

    # identifies the type of bird with the lowest ID number among those with
    # the maximum frequency.
    lowest_id_max_freq = min(
        bird_id for bird_id,
        frequency in counts.items() if frequency == max_frequency)

    return lowest_id_max_freq
