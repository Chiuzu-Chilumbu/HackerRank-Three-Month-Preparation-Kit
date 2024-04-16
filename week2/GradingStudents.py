"""
challenge:  Sam is a professor at the university and likes to 
round each student's  according to these rules:
  If the difference between the  and the next multiple of  is less than , 
  round  up to the next multiple of .
  If the value of  is less than , no rounding occurs as the result will still be a failing grade.
"""


def round_grades(grade: int) -> int:
    next_multiple = grade
    while next_multiple % 5 != 0:
        next_multiple += 1
    
    current_grade = 0
    if (next_multiple - grade) < 3:
        current_grade = next_multiple
    else:
        current_grade = grade

    return current_grade 
        

def gradingStudents(grades):
    # Write your code here
    for index, elements in enumerate(grades):
        if elements >= 37:
            grade = round_grades(elements)
            grades[index] = grade
        else:
            continue
        
    return grades
    

	
grade_arr = [73, 67, 38, 35]
gra_arr = [84, 29, 57]

print(gradingStudents(grade_arr))


print(38 > 38)