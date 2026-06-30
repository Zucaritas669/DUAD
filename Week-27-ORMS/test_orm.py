from repository import UserRepository, CarRepository, AddressRepository

user_repo = UserRepository()
car_repo = CarRepository()
address_repo = AddressRepository()


#Create 

user_repo.create_user("Shalston", "López", "shalston@mail.com", "pass123")
car_repo.create_car("Toyota", "Sedan", 2024)
address_repo.create_address("Nosara, Guanacaste", 1)


#get all
print(user_repo.get_all())
print(car_repo.get_all_car())
print(address_repo.get_all_address())


#associate car with user
car_repo.associate_car_with_user(1,1)


#Edit / Modify
# user_repo.modify_user(1, "Shalston", "Moscoa", "new@mail.com", "newpass")
# print(user_repo.get_all())

# car_repo.modify_car(1,"Nissan", "Sedan", 2024)
# print(car_repo.get_all_car())

# address_repo.edit_address(1,"Samara, Guanacaste", 1)
# print(address_repo.get_all_address())



#delete
# user_repo.delete_user(1)
# car_repo.delete_car(1)
# address_repo.delete_address(1)