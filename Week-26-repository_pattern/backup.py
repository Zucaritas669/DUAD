import os #os → para crear carpetas en tu computadora
import csv
from  datetime import datetime
from db import PgManager


db_manager_backup = PgManager(
    db_name = "postgres",
    user = "postgres",
    password = "postgres",
    host = "localhost"
)


today = datetime.now() .strftime("%Y-%m-%d")
#datetime.now() da la fecha y hora actual completa
#.strftime("%Y-%m-%d") la convierte en texto con el formato deseado


download_path = os.path.join(os.path.expanduser("~"), "Downloads") 
#os.path.join une las rutas de forma segura 
#os.path.expanduser("~") obtiene el home del usuario

backup_folder = os.path.join(download_path, f"db_backup_{today}")

os.makedirs(backup_folder, exist_ok=True)
# crea la carpeta db_backup_{fecha} dentro de Downloads
# si ya existe, no pasa nada



def export_user():
    users = db_manager_backup.execute_query("SELECT * FROM lyfter_car_rental.users")

    with open(f"{backup_folder}/users.csv", "w", newline="", encoding="utf-8") as file:
        write =  csv.writer(file)
        write.writerow(["id", "name", "username", "email", "password", "birth_date", "account_status"]) #header
        write.writerows(users)



def export_cars():
    cars = db_manager_backup.execute_query("SELECT * FROM lyfter_car_rental.cars")

    with open(f"{backup_folder}/cars.csv", "w", newline="", encoding="utf-8") as file:
        write = csv.writer(file)
        write.writerow(["id", "brand", "model", "manufacture_year", "status"])#header
        write.writerows(cars)


def export_rentals():
    rentals = db_manager_backup.execute_query("SELECT * FROM lyfter_car_rental.rentals")

    with open(f"{backup_folder}/rentals.csv", "w", newline="", encoding="utf-8") as file:
        write = csv.writer(file)
        write.writerow(["id", "user_id", "car_id", "rental_date", "rental_status"])#header
        write.writerows(rentals)


export_user()
export_cars()
export_rentals()


# cd Week-26-repository_pattern
# python backup.py