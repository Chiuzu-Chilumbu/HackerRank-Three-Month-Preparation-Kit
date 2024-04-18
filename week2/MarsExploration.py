"""
Challenge:
  A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
  Letters in some of the SOS messages are altered by cosmic radiation during transmission.
  Given the signal received by Earth as a string,'s' ,
  determine how many letters of the SOS message have been changed by radiation.
"""



def marsExploration(s):
    changed_letter_count = 0
    message_length = len(s)
    message = 'SOS'

    for index in range(message_length):
        if s[index] != message[index % 3]:
            changed_letter_count += 1

    return changed_letter_count


s_1 = 'SOSSPSSQSSOR'
s_2 = 'SOSTOT'


print(marsExploration(s_1))