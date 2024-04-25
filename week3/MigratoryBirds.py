"""
Challenge:  Given an array of bird sightings where every element represents a bird type id, 
determine the id of the most frequently sighted type. If more than 1 type has been spotted 
that maximum amount, return the smallest of their ids.
"""

from collections import Counter

def migratoryBirds(arr):
    # Write your code here
    counts = Counter(arr)
    max_frequency = max(counts.values())
    
    lowest_id_max_freq = \
    min(bird_id for bird_id, frequency in counts.items() if frequency == max_frequency)
    
    return lowest_id_max_freq