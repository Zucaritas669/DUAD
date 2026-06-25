from db import PgManager
from faker import Faker  #pip3 install faker
import random

def seed():

    fake = Faker()  
    db = PgManager(
        db_name="postgres",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    if not db.connection:
        print("DB ERROR seed")
        return 
    

    for _ in range(200):  # _ porque no necesitamos el índice
        db.execute_query(
            "INSERT INTO lyfter_car_rental.users (name, username, email, password, birth_date) VALUES (%s,%s,%s,%s,%s)",
            fake.name(),          
            fake.user_name(),     
            fake.email(),         
            fake.password(),      
            fake.date_of_birth(minimum_age=18, maximum_age=80)  
        )
    print("200 users created")


    brands = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Nissan", "Mazda", "Kia", "Hyundai", "Volkswagen"]
    models = ["Sedan", "SUV", "Truck", "Coupe", "Hatchback", "Van", "Convertible"]

    for _ in range(100):
        db.execute_query(
            "INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year) VALUES (%s,%s,%s)",
            random.choice(brands),       
            random.choice(models),       
            random.randint(1990, 2024)  
        )
        #random.choice elige un elemento de una lista. random.randint elige un número de un rango.
    print("100 cars created")


    user_ids = db.execute_query("SELECT id FROM lyfter_car_rental.users")  
    car_ids = db.execute_query("SELECT id FROM lyfter_car_rental.cars")

    rental_count = random.randint(50, 150)  

    for _ in range(rental_count):
        db.execute_query(
            "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s,%s)",
            random.choice(user_ids)[0],  # elige un usuario al azar)
            random.choice(car_ids)[0]    # elige un auto al azar
        )
    print(f"{rental_count} rentals created")

    db.close_connection()

seed()