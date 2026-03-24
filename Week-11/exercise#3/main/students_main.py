from  menu.students_menu import show_menu,get_option
from actions.students_actions import create_student,show_student_information,top_3_average,get_average_from_averages,delete_student,fail_grades
from data.students_data import write_student,read_csv_file

def main():
    students = [] 
    file_path = "write.csv" 

    while True:
        show_menu()
        option  = get_option()

        if option == 1:
            create_student(students)

        elif option == 2:
            show_student_information(students)

        elif option == 3:
            top_3_average(students)
        
        elif option == 4:
            get_average_from_averages(students)
        
        elif option == 5:
            write_student(students,file_path)

        elif option == 6:
            read_csv_file(students, file_path)

        elif option == 7:
            fail_grades(students)
    
        elif option == 8:
            delete_student(students)
        
        elif option == 9:
            break
            
            
            

if __name__ == "__main__":
    main()

#   python -m main.students_main