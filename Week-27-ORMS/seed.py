from db import Session
from models_db import User, Address, Car
from faker import Faker
import random

fake = Faker()

def seed():
    with Session() as s:
        try:
            users = []

            for _ in range(20):
                user = User(
                    name=fake.first_name(),
                    last_name = fake.last_name(),
                    email = fake.email(),
                    password = fake.password()
                )
                s.add(user)
                users.append(user)

            s.commit()
            print("20 users created")


            for user in users:
                address = Address(
                    address=fake.address(),
                    user_id=user.id
                )
                s.add(address)

            s.commit()
            print("20 addresses created")



            brands = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Nissan", "Mazda"]
            models = ["Sedan", "SUV", "Truck", "Coupe", "Hatchback"]

            for i in range(30):

                if i < 20:
                    owner = random.choice(users).id
                else:
                    owner = None
                
                car = Car(
                    brand=random.choice(brands),
                    model=random.choice(models),
                    year=random.randint(1990, 2024),
                    user_id = owner
                    
                    )
                s.add(car)

            s.commit()
            print("30 cars created ")

        except Exception as ex:
            print("Error seeding", ex)

seed()


        

        
