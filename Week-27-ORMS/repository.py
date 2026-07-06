from db import Session
from models_db import User, Address , Car

from sqlalchemy import func

#Notes
#s.query(<name>) -> returns a list of dict so that we need a loop 
#s.get(<name>) -> returns only ONE object/ dict so that we dont need a loop

class UserRepository():

    def create_user(self, name, last_name, email, password):
        with Session() as s:
            try:
                new_user = User(name= name, last_name = last_name, email = email, password= password)  # son necesarios porque SQLAlchemy necesita saber qué valor va a qué columna.
                s.add(new_user)   # marca el objeto como nuevo para insertar
                s.commit()        # confirma el INSERT en la DB
                return True
    
            except Exception as ex:
                print("Error creating user")
                return False



    def edit_user(self, user_id, name, last_name, email, password):
        with Session() as s:
            try:
                user = s.get(User, user_id) # busca el usuario por id
                if not user:
                    print("User not found")
                    return False
                
                user.name = name            # SQLAlchemy detecta los cambios automáticamente
                user.last_name = last_name
                user.email = email
                user.password = password
                s.commit()
                return True
            
            except Exception as ex:
                print("Error modifying user", ex)
                return False
            


    def delete_user(self, user_id):
        with Session() as s:
            try:
                user = s.get(User , user_id) # busca el usuario por id
                if not user:
                    print("User not found")
                    return False
                
                s.delete(user) # marca el objeto para eliminar
                s.commit()
                return True
            
            except Exception as ex:
                print("Error deleting user", ex)
                return False
            


    def get_all(self):
        with Session() as s:
            try:

                users = s.query(User).all()   # SELECT * FROM users
                return [

                    {
                    "id": u.id,
                    "name": u.name,
                    "last_name": u.last_name,
                    "email": u.email
                    } for u in users

                ]

            except Exception as ex:
                print("Error getting users", ex)
                return False


    def get_user_with_car(self):
        with Session() as s:
            try:
                user  = (
                    s.query(User)
                    .join(Car)
                    .group_by(User.id)
                    .having(func.count(Car.id)>1)
                    .all()
                )

                return[
                    {
                    "id": u.id,
                    "name": u.name,
                    "last_name": u.last_name,
                    "email": u.email
                    } for u in user 
                ]

            except Exception as ex:
                print("Error getting car with user")
                return False
            


    def get_cars_and_address(self, id):
        with Session() as s:
            try:
                user = s.get(User, id)
                if not user:
                    print("User not found")
                    return False

                return {

                "id": user.id,
                "name": user.name,
                "cars": 

                [
                    {"id": c.id, "brand": c.brand, "model": c.model}
                    for c in user.car
                ],


                "addresses": 
                [
                    {"id": a.id, "address": a.address}
                    for a in user.address
                ]
            }          

            except Exception as ex:
                print("Error getting Cars and addresses", ex)
                return False



class CarRepository():

    def create_car(self, brand, model, year):
        with Session() as s:
            try:
                new_car = Car(brand=brand, model=model, year=year)
                s.add(new_car)
                s.commit()
                return True
            
            except Exception as ex:
                print("Error creating car")
                return False
    

    def modify_car(self, car_id, brand, model, year):
        with Session() as s:
            try:
                car = s.get(Car, car_id)
                if not car:
                    print("Car not found")
                    return False
                
                car.brand = brand
                car.model = model
                car.year = year
                s.commit()
                return True

            except Exception as ex:
                print("Error editing car")
                return False


    def delete_car(self, car_id):
        with Session() as s:
            try:
                car = s.get(Car, car_id)
                if not car:
                    print("Car not fond")
                    return False
                
                s.delete(car)
                s.commit()
                return True
            
            except Exception as ex:
                print("Error deleting car", ex)
                return False
            

    def associate_car_with_user(self, car_id , user_id):
        with Session() as s:
            try:
                car = s.get(Car, car_id)
                if not car:
                    print("Car not found")
                    return False
                
                user= s.get(User, user_id)
                if not user:
                    print("User not found")
                    return False
                
                car.user_id =  user_id
                s.commit()
                return True
            
            except Exception as ex:
                print("Error associating a car with user", ex)
                return False
            

    def get_all_car(self):
        with Session() as s:
            try:
                
                car = s.query(Car).all()   
                return [
                    {
                        "id" : c.id,
                        "brand" : c.brand,
                        "model" : c.model,
                        "year" : c.year,
                        "user_id" : c.user_id
                    }for c in car
                ]

            except Exception as ex:
                print("Error getting cars", ex)
                return False
            

    def get_cars_without_user(self):
        with Session() as s:
            try:
                car = s.query(Car).filter(Car.user_id == None).all()
                return [
                    {
                        "id" : c.id,
                        "brand" : c.brand,
                        "model" : c.model,
                        "year" : c.year,
                        "user_id" : c.user_id
                    }for c in car
                ]
            except Exception as ex:
                print("Error getting cars without user")
                return False
            


            


class AddressRepository():

    def create_address(self, address, user_id):
        with Session() as s:
            try:

                new_address = Address(address=address, user_id=user_id)
                s.add(new_address)
                s.commit()
                return True
            
            except Exception as ex:
                print("Error creating address", ex)
                return False
            


    def edit_address(self, id, address, user_id):
        with Session() as s:
            try:

                addr = s.get(Address,id)
                if not addr:
                    print("Address not found")
                    return False

                addr.address = address
                addr.user_id = user_id
                s.commit()
                return True
            
            except Exception as ex:
                print("Error editing address", ex)
                return False
            
    
    def delete_address(self, id):
        with Session() as s:
            try:
                address = s.get(Address, id)
                if not address:
                    print("Address not found")
                    return False

                s.delete(address)
                s.commit()
                return True

            except Exception as ex:
                print("Error deleting address",ex)
                return False
            
    
    def get_all_address(self):
        with Session() as s:
            try:
                
                address = s.query(Address).all()   
                return [
                    {
                        "id": a.id,
                        "address": a.address,
                        "user_id": a.user_id,
                    }for a in address
                ]

            except Exception as ex:
                print("Error getting address", ex)
                return False
    


    def filter_by_world(self, word):
        with Session() as s:
            try:
                adr = s.query(Address).filter(Address.address.like(f"%{word}%")) # los % permiten una búsqueda parcial / cualquier cosa antes + palabra + cualquier cosa después

                return [
                {
                    "id": a.id,
                    "address": a.address,
                    "user_id": a.user_id
                } for a in adr
            ]
            except Exception as ex:
                print("Error getting address by word")
                return False
            
