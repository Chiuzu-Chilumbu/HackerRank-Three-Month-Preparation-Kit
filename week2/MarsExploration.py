"""
Challenge:
  A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
  Letters in some of the SOS messages are altered by cosmic radiation during transmission.
  Given the signal received by Earth as a string,'s' ,
  determine how many letters of the SOS message have been changed by radiation.
"""


def marsExploration(s: str) -> int:
    """
    Determines the number of letters in a message that were altered during transmission.

    Args:
    s (str): The received message.

    Returns:
    int: The count of altered letters in the message.
    """
    
    # Initialize a variable to count the number of altered letters
    changed_letter_count = 0
    
    # Get the length of the received message
    message_length = len(s)
    
    # Define the expected message pattern
    message = 'SOS'

    # Iterate through each letter in the received message
    for index in range(message_length):
        # Check if the current letter is different from the expected letter in the pattern
        if s[index] != message[index % 3]:
            # Increment the count of altered letters
            changed_letter_count += 1

    return changed_letter_count
