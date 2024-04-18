"""
challenge:  Sam is a professor at the university and likes to 
round each student's  according to these rules:
  If the difference between the  and the next multiple of  is less than , 
  round  up to the next multiple of .
  If the value of  is less than , no rounding occurs as the result will still be a failing grade.
"""
from typing import List

def round_grades(grade: int) -> int:
    """
    Rounds a given grade according to the specified rules.

    Args:
    grade (int): The grade to be rounded.

    Returns:
    int: The rounded grade.
    """
    next_multiple = grade
    # Find the next multiple of 5 greater than or equal to the given grade
    while next_multiple % 5 != 0:
        next_multiple += 1
    
    current_grade = 0
    # Determine if rounding is necessary based on the difference between the next multiple of 5 and the given grade
    if (next_multiple - grade) < 3:
        current_grade = next_multiple
    else:
        current_grade = grade

    return current_grade
        

def gradingStudents(grades: List[int]) -> List[int]:
    """
    Rounds each grade in the list according to the specified rules.

    Args:
    grades (list): A list of student grades.

    Returns:
    list: The list of grades after rounding.
    """
    # Iterate through each grade in the list
    for index, elements in enumerate(grades):
        # Check if the grade is eligible for rounding
        if elements >= 37:
            # Round the grade using the round_grades function
            grade = round_grades(elements)
            # Update the grade in the list
            grades[index] = grade
        else:
            # If the grade is less than 37, no rounding occurs
            continue
        
    return grades
