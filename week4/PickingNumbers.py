"""
Challenge: 

"""

def pickingNumbers(a):
    # decalre variables
    frequency = {}
    
    # obtain the frequencey of the elements in the list
    for element in a:
        if element in frequency:
            frequency[element] += 1
            
        else:
            frequency[element] = 1
            
    
    # initialize the maximum length
    max_length = 0

    # iterate through the frequency dictionary
    for numbers in frequency:
        # curerent length is the frequenct of the first number because 
        # it subtracts itself and equates to 0 which is less that 1
        current_length = frequency[numbers]

        # check for the next number in the sequence and if it is 1 value greater we add it to the current length
        if numbers + 1 in frequency:
            current_length += frequency[numbers + 1]

        # check if the current length is greater than the max length
        max_length = max(max_length, current_length)
        
    return max_length
        
    