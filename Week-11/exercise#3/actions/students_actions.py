import re

class Student():
    def __init__(self,name,section,subject):

        self.name = name
        self.section = section
        self.subject = subject
        

def validate_name():
    while True:
        name = input("Name ➾ ").strip()
        if name.replace(" ","").isalpha():
            return name
        print("\n⚠︎ Invalid format; Please try again ⚠︎")


def validate_section():
    while True:
        section = input("Section ➾ ").strip().upper()
        if re.fullmatch(r"\d{1,2}[A-Z]", section):
            return section
        print("\n⚠︎ Invalid section format. Example: 10B ⚠︎")


def validate_grade(subject):
    while True:
        try:
            grade = int(input(f"{subject} ➾  "))
            if 0 <= grade <= 100:
                return grade
            print("\n⚠︎ The subject grade must be between 0 and 100 ⚠︎")
        except ValueError as ex:
            print(f"\n⚠︎ Invalid grade ⚠︎ \n{ex}")



def student_name():
    print("")
    print('='*30)
    print("     Student info     ")
    print('='*30)
    return validate_name()          # ← antes era el while True completo


def student_section():
    return validate_section()       # ← antes era el while True completo


def student_subjects():
    print("")
    print('='*30)
    print("     Student Subjects     ")
    print('='*30)

    subject_list = ["Spanish","English","Social Studies","Science"]
    subjects_dict = {}

    for subject in subject_list:
        subjects_dict[subject] = validate_grade(subject)  # ← antes era el while True completo

    return subjects_dict

# def student_name():
#     print("")
#     print('='*30)
#     print("     Student info     ")
#     print('='*30)

#     while True:
#         name = input("Name ➾ ").strip()
#         if name.replace(" ","").isalpha():
#             break
#         else:
#             print("\n⚠︎ Invalid format; Please tyr again ⚠︎")
#     return name


# def student_section():
#     while True:
#         section = input("Section ➾ ").strip().upper()

#         if re.fullmatch(r"\d{1,2}[A-Z]", section):
#             return section
#         else:
#             print("\n⚠︎ Invalid section format. Example: 10B ⚠︎")


# def student_subjects():

#     print("")
#     print('='*30)
#     print("     Student Subjects     ")
#     print('='*30)

#     subject_list = ["Spanish","English","Social Studies","Science"]
#     subjects_dict = {}

#     for subject in subject_list:
#         while True:
#                 try: 
#                     grade = int(input(f"{subject} ➾  "))
#                     if grade > 100 or grade < 0:
#                         print("\n⚠︎ The subject grade must be less than 100 or greater than 0 ⚠︎")
#                     else:
#                         break
#                 except ValueError as ex:
#                     print(f"\n⚠︎ Invalid grade ⚠︎ \n{ex} ")

#         subjects_dict[subject] = grade
#     return subjects_dict


def create_student(students):

    while True:
        try:
            n = int(input("\nHow many students do you want to add? ➾  "))
            if n > 0:
                break
            print("\n⚠︎ Must be greater than 0 ⚠︎")
        except ValueError:
            print("\n⚠︎ Please enter a valid number ⚠︎")

    for i in range(1, n + 1):
        print(f"\n--- Student {i} of {n} ---")

        name = student_name()
        section = student_section()

        duplicate = any(
            s.name.strip().lower() == name.strip().lower() and
            s.section.strip().upper() == section.strip().upper()
            for s in students
        )
        if duplicate:
            print("\n⚠︎ Student already exists, skipping ⚠︎")
            continue

        subjects = student_subjects()

        student  = Student(name,section,subjects)

        students.append(student)

        print("➾ Student added correctly")


def show_student_information(students):

    print('='*30)
    print("     Student information     ")
    print('='*30)

    for student in students:
        print("-"*30)
        print(f'Name ➾ {student.name}')
        print(f'Section ➾ {student.section}')
        print('Subjects ↴')

        for key, value in student.subject.items():
            print(f"{key} ➾ {value}")


def top_3_average(students):

    if not students:
        print("⚠︎ Not students added ⚠︎")
        return

    top_3_list = [] 
    average = None

    for student in students:
        average = sum(student.subject.values()) / len(student.subject)
        top_3_list.append((average,student))

    top_3_list.sort(key=lambda item: item[0], reverse=True)

    print("\n TOP 3 STUDENTS ")
    for average,student in top_3_list[:3]:
        print(student.name, "-", round(average, 2))

    return top_3_list[:3]




def get_average_from_averages(students):

    if not students:
        print("⚠︎ No students added ⚠︎")
        return
    
    total = 0

    for s in students:
        average = sum(s.subject.values()) / len(s.subject)
        total += average

    total = total / len(students)

    print(f"\nAverage of Averages ➾ {total}")

    return total




def delete_student(students): 

    name = student_name()
    section = student_section()

    for s in students:
        if s.name.strip().lower() == name.strip().lower() and s.section.strip().upper() == section.strip().upper():
            option = input("Student founded; DO you want to delete them? (y/n)\n ➾ ").lower()

            if option == "y":
                students.remove(s)
                print("Student deleted successfully!")

            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")

            
            


def fail_grades(students):

    print('='*30)
    print("     Failed grades     ")
    print('='*30)

    for student in students:
        
            if any(grade < 60 for grade in student.subject.values()):
                print("-"*30)
                print(f'Name ➾ {student.name}')
                print(f'Section ➾ {student.section}')

                for key, value in student.subject.items():  
                    if value < 60: 
                        print(f"{key} ➾ {value}" )
    
    return students
