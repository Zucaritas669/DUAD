current_grade = 0
notes_counter = 1
number_of_passed_grades = 0
number_of_failed_grades = 0
average_passed_grades = 0
average_failed_grades = 0
total_average = 0


total_grades = int(input('Type the total number of grades: '))

while (notes_counter <= total_grades):

    current_grade = int(input(f'Type the grade {notes_counter}: '))
    
    if(current_grade < 70):
        number_of_failed_grades = number_of_failed_grades + 1
        average_failed_grades = average_passed_grades + current_grade
    else:
        number_of_passed_grades = number_of_passed_grades + 1
        average_passed_grades = average_passed_grades + current_grade

        total_average = total_average +(current_grade/total_grades)
    
    notes_counter += 1

    
    
if(number_of_failed_grades>0) :
    average_failed_grades /= number_of_failed_grades

if(number_of_passed_grades > 0):
    average_passed_grades /= number_of_passed_grades

print(f'Number of passed grades: {number_of_passed_grades}')
print(f'Average of passed grades: {average_passed_grades}')

print(f'Number of failed grades: {number_of_failed_grades}')
print(f'average of failed grades: {average_failed_grades}')

print(f'Total average: {total_average}')