"""
Challenge : There is a collection of input strings and a collection of query strings. 
  For each query string, determine how many times it occurs in the list of input strings. 
  Return an array of the results.

"""

def matchingStrings(strings: list, queries:list ):
    """
    Counts how many times each query string appears in the list of strings.

    Args:
    strings (list): The list of string elements to search within.
    queries (list): The list of query strings to search for in the strings list.

    Returns:
    list: A list of integers representing the count of each query string's occurrence in the strings list.
    """
    
    # Declare needed variables
    instance_occurs = [] 
    current_query_index = 0 
    
    # loop through the queries by index and ensure not to exceed the list index
    while current_query_index < len(queries):
        # set our first query to the first string in the list
        current_query = queries[current_query_index]
        instance_counter = 0
        
		# loop through the strings array and count how many times the query exists
        for string in strings:
            if current_query == string:
                # update the numbers of instances 
                instance_counter += 1
        # append the final instance count
        instance_occurs.append(instance_counter)
        # proceed to next query
        current_query_index += 1