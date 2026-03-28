employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]


department_per_employee = {}

for data in employees:
    department = data["department"]
    name = data["name"]

    if department not in department_per_employee:
        department_per_employee[department] = [name]
    else:
        department_per_employee[department].append(name)

print(department_per_employee)