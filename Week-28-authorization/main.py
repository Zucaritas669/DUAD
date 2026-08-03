from flask import  Flask , request, jsonify
from repositories.user_repository import UserRepository
from repositories.item_repository import ItemRepository
from repositories.invoice_repository import InvoiceRepository

from auth.decorators import login_required , admin_required
from cache import CacheManager
import json

user_repo = UserRepository()
item_repo = ItemRepository()
invoice_repo = InvoiceRepository()

cache_manager = CacheManager(host="PLACEHOLDER", port="PLACEHOLDER", password="PLACEHOLDER")

app = Flask(__name__)
#code
@app.route("/me", methods = ["GET"])
@login_required # Valida el token. Si es válido
def me():
    try:
        # Extrae el user_id del token (que está guardado en request.user por @login_required)
        user = user_repo.get_user_by_id(request.user["user_id"])
        if not user:
            return jsonify(message="User not found"), 404
        
        return jsonify(
            id=user.id,
            name=user.name,
            email=user.email,
            role=user.role
        ), 200
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    

@app.route("/login", methods = ["POST"])
def login():
    try:
        valid  = ["email", "password"]

        for l in valid:
            if l not in request.json or not request.json[l]:
                return jsonify(message = f"{l} is missing"),400
            
        token = user_repo.login(request.json["email"], request.json["password"])

        if not token:
                return jsonify(message="Invalid credentials"), 401
            
        return jsonify(token=token),200
        
    except ValueError as ex:
        return jsonify(message = str(ex)),400
    except Exception as ex:
        return jsonify(message = str(ex)),500



@app.route("/user", methods = ["POST"])
def create_user_flask():
    try:

        valid_request = ["name", "user_name", "email", "password", "role"]

        for u in valid_request:
            if u not in request.json or not request.json[u]:
                return jsonify(message = f"{u} is required"),400
            
        valid_roles = ["admin", "user"]
        if request.json["role"] not in valid_roles:
            return jsonify(message = "Invalid role (Valid roles admin/user)"),400
        
        user = user_repo.create_user(
            name = request.json["name"],
            user_name = request.json["user_name"],
            email= request.json["email"],
            password= request.json["password"],
            role = request.json["role"]
        )
        if not user:
            return jsonify(message = "Email already exist"),409
        return jsonify(message = "User created"),201
    
    except ValueError as ex:
        return jsonify(message = str(ex)), 400
    except Exception as ex:
        return jsonify(message = str(ex)), 500


@app.route("/user/<int:id>", methods = ["GET"])
@login_required
@admin_required
def get_user_by_id_flask(id):
    try:
        user = user_repo.get_user_by_id(id)
        if not user:
            return jsonify(message = "User not found"),404
        
        return jsonify(
            id = user.id,
            name = user.name,
            user_name = user.user_name,
            email=user.email,
            role=user.role
        ),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500


@app.route("/user", methods = ["GET"])
@login_required
@admin_required
def get_user_by_email_flask():
    try:
        email = request.args.get("email")
        if not email:
            return jsonify(message = "Email required"),400
        

        user = user_repo.get_user_email(email)
        if not user:
            return jsonify(message = "User not found"),404
        
        return jsonify(
            id = user.id,
            name = user.name,
            user_name = user.user_name,
            email=user.email,
            role=user.role
        ),200
    
    except ValueError as ex:
        return jsonify(message = str(ex)),400
    except Exception as ex:
        return jsonify(message = str(ex)),500

#==============================================================================
@app.route("/item", methods = ["POST"])
@login_required
@admin_required
def create_item_flask():
    try:
        valid_body = ["name", "price", "stock"]

        for i in valid_body:
            if i not in request.json or not request.json[i]:
                return jsonify(messaged= f"{i} is missing"),400
            
        if request.json["price"] <= 0:
            return jsonify(messaged= "Price can not be 0"),400
        if request.json["stock"] <= 0:
            return jsonify(messaged= "Stock can not be 0"),400
        
        item = item_repo.create_item(
            name  = request.json["name"],
            price = request.json["price"],
            stock = request.json["stock"]
        )
        cache_manager.delete_data("items:all")
        #como se agrega una fruta nueva, se borra la lista existente



        return jsonify(message = "Item created"), 201
    except ValueError as ex:
        return jsonify(message = str(ex)),400
    except Exception as ex:
        return jsonify(message = str(ex)),500
    

@app.route("/item/<int:id>",methods = ["GET"])
def get_item_by_id_flask(id):
    try:

        key = f"item:{id}"
        # Arma una clave única de Redis para esta fruta específica

        exist,tll = cache_manager.check_key(key)
        if exist:
            cached = cache_manager.get_data(key)
            return jsonify(json.loads(cached)), 200
        # Si existe, la trae de Redis
        # La convierte de string a dict y la retorna, sin tocar Postgres , por eso el json.loads


        fruit = item_repo.get_item_by_id(id)
        if not fruit:
            return jsonify(message = "Item not found"),404
        
        data = {
            "id": fruit.id,
            "name": fruit.name,
            "price": float(fruit.price),
            "stock": fruit.stock
        }
        cache_manager.store_data_redis(key, json.dumps(data))
        return jsonify(data), 200
    # Guarda esa fruta en Redis como string, para la próxima consulta
    
    except Exception as ex:
        return jsonify(message = str(ex)),500
    

@app.route("/item",methods = ["GET"])
def get_all_items_flask():
    try:

        key = "items:all"
        exists, ttl = cache_manager.check_key(key)
        # Arma una clave única de Redis
        # Revisa si ya existe la lista cacheada

        if exists:
            cached = cache_manager.get_data(key)
            return jsonify(json.loads(cached)), 200
            # Si existe, la trae de Redis
            # La convierte de string a dict y la retorna, sin tocar Postgres , por eso el json.loads


        item = item_repo.get_all_items()
        if not item:
            return jsonify(message = "No item"),404
        
        items_list = []
        for i in item:
            items_list.append({
                "id": i.id,
                "name": i.name,
                "price": float(i.price),
                "stock": i.stock
            })
        cache_manager.store_data_redis(key, json.dumps(items_list))
        return jsonify(items_list),200
        # Guarda la lista completa en Redis para la próxima consulta

        
    except Exception as ex:
        return jsonify(message = str(ex)),500


@app.route("/item/<int:id>",methods = ["PATCH"])
@login_required
@admin_required
def edit_item_flask(id):
    try:
        valid_body = ["name", "price", "stock"]

        for i in valid_body:
            if i not in request.json or not request.json[i]:
                return jsonify(messaged= f"{i} is missing"),400
            
        if request.json["price"] <= 0:
            return jsonify(messaged= "Price can not be 0"),400
        if request.json["stock"] <= 0:
            return jsonify(messaged= "Stock can not be 0"),400
        
        item = item_repo.edit_item(
            id = id ,
            name = request.json["name"],
            price=  request.json["price"],
            stock = request.json["stock"],
            
        )  
        if not item:
            return jsonify(message= "Item not found"),404


        cache_manager.delete_data(f"item:{id}")
        # La fruta editada ya no coincide con lo que había en cache

        cache_manager.delete_data("items:all")
        # La lista completa tampoco es correcta, porque incluye esta fruta desactualizada
        return jsonify(message= "Item updated"),200
    

    except ValueError as ex:
        return jsonify(message = str(ex)),400
    except Exception as ex:
        return jsonify(message = str(ex)),500


@app.route("/item/<int:id>",methods = ["DELETE"])
@login_required
@admin_required
def delete_item_flask(id):
    try:
        item = item_repo.delete_item(id)
        if not item:
            return jsonify(message = "Item not found"),404
        
        cache_manager.delete_data(f"item:{id}")
        # Borra la versión cacheada de esta fruta

        cache_manager.delete_data("items:all")
        # Borra la lista completa cacheada
        
        return jsonify(message = "Item deleted"),200
    except Exception as ex:
        return jsonify(message = str(ex)),500

#==============================================================================

@app.route("/purchase",methods = ["POST"])
@login_required
def create_purchase_flask():
    try:
        valid = ["items"]
        for i in valid:
            if i not in request.json or not request.json[i]:
                return jsonify (message = f"{i} is missing"),400
        
            
        invoice = invoice_repo.create_purchase(
            user_id = request.user["user_id"],
            items = request.json["items"]
        )

        return jsonify(
            message = "Purchase completed",
            invoice_id = invoice.id,
            user_id = invoice.user_id,
            total = float(invoice.total)
        ),201
    

    except ValueError as ex:
        return jsonify(message = str(ex)),400
    except Exception as ex:
        return jsonify(message = str(ex)),500


@app.route("/invoice/<int:id>",methods = ["GET"])
@login_required
def get_user_invoices_flask(id):
    try:

        if request.user["role"] == "user" and request.user["user_id"] != id:
            return jsonify(message = "Forbidden: can only view your invoices"),404
        

        user = invoice_repo.get_invoices(id)
        if not user:
            return jsonify(message = "User not found"),404
        
        invoice_list = []
        for i in user:
            invoice_list.append({
                "id": i.id,
                "user_id" : i.user_id,
                "total" : float(i.total),
                "created_at" : i.created_at
            })
        return jsonify(invoice_list),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500


@app.route("/invoice",methods = ["GET"])
@login_required
@admin_required
def get_all_invoices_flask():
    try:
        user = invoice_repo.get_all_invoices()
        if not user:
            return jsonify(message = "User not found"),404
        
        invoice_list = []
        for i in user:
            invoice_list.append({
                "id": i.id,
                "user_id" : i.user_id,
                "total" : float(i.total),
                "created_at" : i.created_at
            })
        return jsonify(invoice_list),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500


#code
if __name__ == "__main__":
    app.run(host="localhost", debug=True)

#cd Week-28-authorization

    # "name":"Manchas",
    # "user_name":"spots",
    # "email": "manchas@gmail.com",
    # "password": "1234",
    # "role" : "admin"


#    "name": "Rex",
#    "user_name": "Rexy",
#    "email": "rex@gmail.com",
#    "password": "1234",
#    "role": "admin"