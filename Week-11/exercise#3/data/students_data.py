import csv
import os 
from actions.students_actions import Student


def write_student(students,file_path):

    if not students:
        print("⚠︎ There are no students to export ⚠︎")
        return
    
    headers = (
        "name",
        "section",
        "Spanish",
        "English",
        "Social Studies",
        "Science",
    ) 
    data = []


    for s in students:
        row = {}

        row["name"] = s.name
        row["section"] = s.section

        row["Spanish"] = s.subject["Spanish"]
        row["English"] = s.subject["English"]
        row["Social Studies"] = s.subject["Social Studies"]
        row["Science"] = s.subject["Science"]

        data.append(row)



    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print("Students exported successfully!")


# Crea una lista vacía data
# Recorre cada estudiante
# Crea una fila nueva (row)
# Copia nombre, sección y notas
# Guarda esa fila en data
# Escribe todas las filas en el CSV



def read_csv_file(students, file_path):   

    if not os.path.exists(file_path):
        print("⚠︎ File not found ⚠︎")
        return 
    
    with open(file_path,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            subjects = {
                "Spanish":       int(row["Spanish"]),
                "English":       int(row["English"]),
                "Social Studies":int(row["Social Studies"]),
                "Science":       int(row["Science"])
            }

            student = Student(row["name"] ,row["section"], subjects)
            students.append(student)


    print("Students imported successfully!")





    


