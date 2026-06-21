class UserRepository():
    def __init__(self, db_manager):
        self.db_manager = db_manager

        #esta lista es para hacer los filtros , se estabalece una lista con las columnas que se permiten filtrar
        self.allowed_filters = ["name", "username", "email", "account_status"]
        



    def _format_user(self, user_record): 
        #lleva _ porque solo se usa en esta clase
        return{
            "id":user_record[0],
            "name":user_record[1],
            "username":user_record[2],
            "email":user_record[3],
            "password":user_record[4],
            "birth_date":user_record[5],
            "account_status":user_record[6]
        }
    
    
    def create_user(self, name, username, email, password, birth_date):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (name, username, email, password, birth_date) VALUES (%s,%s,%s,%s,%s)",
                name, username, email, password, birth_date 
            )
            return True
        
        except Exception as ex:
            print("Error creating user",ex)
            return False


    def change_user_status(self, account_status, user_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s",
                account_status, user_id
            )
            return True
        except Exception as ex:
            print("Error changing user acount status", ex)
            return False
        

    def morose_flag(self, user_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s",
                "morose", user_id
            )
            return True
        except Exception as ex:
            print("Error flagging user as morose",ex)
            return False
        

    def get_all(self, filters=None):                    # filters es opcional: None = traer todo
        try:
            query = "SELECT id, name, username, email, password, birth_date, account_status FROM lyfter_car_rental.users" # query base sin filtro
            args = []                                   # acá van los valores de los filtros

            if filters:
                condition = []                          # acá van las condiciones del WHERE
                for key,value in filters.items():       # recorre cada filtro (columna y valor)
                    if key in self.allowed_filters:     # solo columnas permitidas 
                        condition.append(f"{key}= %s")  # arma "columna = %s
                        args.append(value)              # guarda el valor para el %s

                if condition:                           # si hubo al menos un filtro válido
                    query += " WHERE " + " AND ".join(condition)    # pega el WHERE al query
            results = self.db_manager.execute_query(query, *args)   # ejecuta el query con los valores
            return [self._format_user(r) for r in results]  # convierte tuplas en dicts
        except Exception as ex:
            print("Error getting users", ex)     # si algo falla, lo muestra
            return False            

class CarRepository():
    def __init__(self, db_manager):
        self.db_manager = db_manager

        self.allowed_filter_cars = ["brand", "model", "manufacture_year", "status"]

    
    def _format_car(self,car_record):
        return{
            "id":car_record[0],
            "brand":car_record[1],
            "model":car_record[2],
            "manufacture_year":car_record[3],
            "status":car_record[4],
        }
    

    def create_car(self, brand, model, manufacture_year):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year) VALUES (%s,%s,%s)",
                brand, model, manufacture_year
            )
            return True
        except Exception as ex:
            print("Error creating a new car", ex)
            return False
        

    def change_status(self, status , car_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s",
                status,car_id
            )
            return True
        except Exception as ex:
            print("Error updating car status", ex)
            return False
        

    def get_all_cars(self, filters=None):
        try:
            query = "SELECT id, brand, model, manufacture_year, status FROM lyfter_car_rental.cars"
            args = []

            if filters:
                condition = []
                for key , value in filters.items():
                    if key in self.allowed_filter_cars:
                        condition.append(f"{key}=  %s")
                        args.append(value)

                if condition:
                    query += " WHERE " + " AND " .join(condition)
            results = self.db_manager.execute_query(query, *args)
            return [self._format_car(r) for r in results]
        
        except Exception as ex:
            print("Error getting cars", ex)     
            return False 

        


class RentalRepository():
    def __init__ (self, db_manager):
        self.db_manager = db_manager

        self.allowed_rentals = ["user_id", "car_id", "rental_date", "rental_status"]

    def _format_rental(self,rental_record):
        return {
            "id":rental_record[0],
            "user_id":rental_record[1],
            "car_id":rental_record[2],
            "rental_date":rental_record[3],
            "rental_status":rental_record[4]
        }
    
    def create_rental(self, user_id, car_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (user_id, car_id) VALUES (%s,%s)",
                user_id , car_id
            )
            return True
        except Exception as ex:
            print("Error creating a new rental", ex)
            return False
        

    def complete_rental(self, rental_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s",
                "completed", rental_id
                #como queremos que simpre sea completed , se pasa de una vez y no se pasa parámetro
                #El ususrio no debe de ingresar o elegir es solo una opcion y punto
            )
            return True
        except Exception as ex:
            print("Error changing rental status",ex)
            return False

    #Este me parece que es redundante
    def change_status_rental(self, rental_status, rental_id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s",
                rental_status,rental_id
            )
            return True
        except Exception as ex:
            print("Error changing rental status", ex) 
            return False
        
    
    def get_rentals(self, filters=None):
        try:
            query = "SELECT id, user_id, car_id, rental_date, rental_status FROM lyfter_car_rental.rentals"
            args = []

            if filters:
                condition = []
                for key , value in filters.items():
                    if key in self.allowed_rentals:
                        condition.append(f"{key}=  %s")
                        args.append(value)

                if condition:
                    query += " WHERE " + " AND " .join(condition)
            results = self.db_manager.execute_query(query, *args)
            return [self._format_rental(r) for r in results]
        
        except Exception as ex:
            print("Error getting rentals", ex)     
            return False 