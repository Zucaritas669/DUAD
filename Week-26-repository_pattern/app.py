
from flask import Flask, request , jsonify
from db import PgManager
from repository import UserRepository , CarRepository, RentalRepository

# cd Week-26-repository_pattern
# python app.py

app = Flask(__name__)
#code

# Creamos (instanciamos) el PgManager con los datos de conexión a la base.
# Luego se lo pasamos al Repository para que pueda hacer sus queries.
db_manager = PgManager(
    db_name = "postgres",
    user = "postgres",
    password = "postgres",
    host = "localhost"
)
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rental_repo = RentalRepository(db_manager)
#==========================================  CREATE Routes ================================

#========== Create USER ==============
@app.route("/users", methods=["POST"])
def create_user():
    try:

        if not request.json:                         
            raise ValueError("No JSON body provided")
        

        
        if "name" not in request.json:
            raise ValueError("name missing")
        
        if "username" not in request.json:
            raise ValueError("username missing")
        
        if "email" not in request.json:
            raise ValueError("email missing")
        
        if "password" not in request.json:
            raise ValueError("password missing")
        
        if "birth_date" not in request.json:
            raise ValueError("birth_date missing")
        
        result = user_repo.create_user(
            request.json["name"],
            request.json["username"],
            request.json["email"],
            request.json["password"],
            request.json["birth_date"]
        )
        if not result:
            return jsonify(message  = "Could not create a user"), 500

        return {"Status":"User created"},201
    except ValueError as ex:
        return jsonify(message = str(ex)),400

#========== Create CAR ===============
@app.route("/cars", methods = ["POST"])
def create_car():
    try:

        if not request.json:                          
            raise ValueError("No JSON body provided")


        if "brand" not in request.json:
            raise ValueError("Brand missing")
        
        if "model" not in request.json:
            raise ValueError("Model missing")  
        
        if "manufacture_year" not in request.json:
            raise ValueError("manufacture_year missing")  
        
        result = car_repo.create_car(
            request.json["brand"],
            request.json["model"],
            request.json["manufacture_year"]
        )
        if not result:
            return jsonify(message  = "Could not create a car"), 500

        return {"Status":"Car created"},201
    except ValueError as ex:
        return jsonify(message = str(ex)),400


#========== Create rental ===============
@app.route("/rentals", methods = ["POST"])
def create_rental():
    try:

        if not request.json:                          
            raise ValueError("No JSON body provided")


        if "user_id" not in request.json:
            raise ValueError("User_id missing")
        
        if "car_id" not in request.json:
            raise ValueError("Car_id missing")
        
        result= rental_repo.create_rental(
            request.json["user_id"],
            request.json["car_id"],
        )
        if  not result:
            return jsonify(message  = "Could not create a rental"), 500
        
        return{"Status":"Rental created"},201
    except ValueError as ex:
        return jsonify(message = str(ex)),400
    

#==========================================  MODIFY Routes ================================

#========== Change car status =====================
valid_status = ["available", "rented", "disabled"]

@app.route("/cars/<int:car_id>", methods = ["PATCH"])
def change_car_status(car_id):
    try:

        if not request.json:                          
            raise ValueError("No JSON body provided")
        

        if "status" not in request.json:
            raise ValueError("Status missing")
        
        if request.json["status"] not in valid_status:
            raise ValueError("Invalid status")
        

        result  = car_repo.change_status(request.json["status"],car_id) # car_id es para verificar cual auto es
        if not result:
            return jsonify(message  = "Could not update car status"), 500

        return {"Status": "Car status updated"}, 200
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    

    
#========== Change user status =====================
valid_account_status = ["active", "disabled", "morose"]

@app.route("/users/<int:user_id>",methods = ["PATCH"])
def change_user_account_status(user_id):
    try:

        if not request.json:                          
            raise ValueError("No JSON body provided")


        if "account_status" not in request.json:
            raise ValueError("Account status missing")
        
        if request.json["account_status"] not in valid_account_status:
            raise ValueError("Invalid account status")
        
        result=user_repo.change_user_status(request.json["account_status"],user_id)
        if not result:
            return jsonify(message  = "Could not update user  status"), 500

        return{"Status":"User account status updated"},200
    except ValueError as ex:
        return jsonify(message = f"Error with the endpoint {ex}"),400



#========== Change rental status =====================

@app.route("/rentals/<int:rental_id>/completed", methods = ["PATCH"])
def rental_status_completed(rental_id):

    result = rental_repo.complete_rental(rental_id)
    if not result:
        return jsonify(message  = "Could not update rental  status"), 500
    
    return {"Status":"Rental completed"},200

#Por que se hace así?
#Se hace así porque queremos marcar el status como "completed" sin mas,
#no hay mas opciones, entonces no se cpmprueba nada ni request , ya que es un estado único

#Adicionalmente se pasa el valor al app.rout de ina vez sin tanta complicaión


#========== Change rental status 2 =====================
rental_status = ["active","canceled"]

@app.route("/rentals/<int:rental_id>", methods = ["PATCH"])
def change_status_rental_two(rental_id):
    try:

        if not request.json:                          
            raise ValueError("No JSON body provided")


        if "rental_status" not in request.json:
            raise ValueError("Rental Status missing")
        
        if request.json["rental_status"] not in rental_status:
            raise ValueError("Invalid rental Status")
        

        result  = rental_repo.change_status_rental(request.json["rental_status"],rental_id)
        if not result:
            return jsonify(message  = "Could not update rental  status"), 500
    
        return{"Status":"Rental Status changed"},200
    except ValueError as ex:
        return jsonify(message = f"Error with the endpoint {ex}"),400


#========== Change user status morose =====================
@app.route("/users/<int:user_id>/morose", methods = ["PATCH"])
def morose_status(user_id):
        
        result = user_repo.morose_flag(user_id)
        if not result:
            return jsonify(message  = "Could not update user status"), 500
    
        return {"Status":"Morose status updated"},200



#==========================================  filter Routes ================================

@app.route("/users", methods=["GET"])
def list_users():
    filters = request.args.to_dict()    # agarra todos los query params como dict
    users = user_repo.get_all(filters) # se los pasa al repo

    if users is False:  # Por que es is false? porque una lista vacía [] también es false, y no es un error
        return jsonify(message = "could not get users"),500

    return {"users": users}, 200


@app.route("/cars", methods = ["GET"])
def get_all_cars():
    result = request.args.to_dict()
    cars = car_repo.get_all_cars(result)

    if cars is False:
        return jsonify(message = "could not get cars"),500

    return {"cars":cars},200


@app.route("/rentals",methods = ["GET"])
def get_all_rentals():
    result = request.args.to_dict()
    rental = rental_repo.get_rentals(result)

    if rental is False:
        return jsonify(message = "could not get rentals"),500
    return {"rentals":rental}




#code
if __name__ == "__main__":
    app.run(host ="localhost", debug=True)






