


from flask import Flask ,jsonify, request
from Repo.user_repository import UserRepository 
from Repo.category_repository import CategoryRepository
from Repo.item_repository import ItemRepository
from Repo.address_repository import AddressRepository
from Repo.paymethod_repository import PayMethodRepository
from Repo.cart_repository import CartRepository
from Repo.invoice_repository import InvoiceRepository
from Repo.return_repository import ReturnRepository

from Auth.decorators import admin_required, login_required 
from DB.cache_redis import CacheManager
import json

user_repo = UserRepository()
category_repo = CategoryRepository()
item_repo = ItemRepository()
address_repo = AddressRepository()
pay_repo = PayMethodRepository()
cart_repo = CartRepository()
invoice_repo = InvoiceRepository()
return_repo = ReturnRepository()


import os
from dotenv import load_dotenv
load_dotenv()
cache_manager = CacheManager(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD")
)

app = Flask(__name__)




#===============================================================================================================================
#                                                       USER ENDPOINTS
#===============================================================================================================================


@app.route("/register",methods = ["POST"])
def create_user():
    try:
        valid = ["name", "username", "email", "password"]
        for u in valid:
            if u not in request.json or not request.json[u]:
                return jsonify(message = f"{u} is missing"),400

        user = user_repo.register(
            name = request.json["name"],
            username =  request.json["username"],
            email = request.json["email"],
            password = request.json["password"]
        )
        if user is False:
            return jsonify(message = "Email already exist"),409
        if user is None:
            return jsonify(message = "User name already exist"),409
        
        return jsonify(message = "User created"),201
    
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/login", methods =["POST"])
def login():
    try:
        valid = ["email", "password"]
        for v in valid:
            if v not in request.json or not request.json[v]:
                return jsonify(message = f"{v} is missing"),400

        token = user_repo.login(request.json["email"], request.json["password"])
        if token is False:
            return jsonify(message = "Invalid token"),401

        if token == "User is deactivated":
            return jsonify(message = "User is deactivated"),403
        return jsonify(token = token ),200
            
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500



@app.route("/user/<int:id>",methods = ["PATCH"])
@login_required
@admin_required

def edit_user_flask(id):
    try:
        valid = ["name","username","email","password",]
        for v in valid:
            if v not in request.json or not request.json[v]:
                return jsonify(message = f"{v} is missing"),400


        user = user_repo.edit_user(
            id = id,
            name = request.json["name"],
            username = request.json["username"],
            email = request.json["email"],
            password=  request.json["password"]
            )
        if user is False:
            return jsonify(message = "User not found"),404 

        if user == "This is an admin account, only the developer can edit it":
            return jsonify(message = "Forbidden ,only developer"),403
        
        if user == "This username already exist":
            return jsonify(message = "This username already exist"),409
        
        if user == "This email already exist":
            return jsonify(message = "This email already exist"),409

        return jsonify(message = f"User edited"),200
        
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500


@app.route("/user/delete/<int:id>",methods = ["DELETE"])
@login_required
@admin_required
def delete_user(id):
    try:
        user = user_repo.soft_delete_user(id)
        if user is False:
            return jsonify(message = "User not found"),404

        if user == "This is an admin account, only the developer can delete it":
            return jsonify(message = "Forbidden, only developer"),403

        if user =="This user has an active Cart":
            return jsonify(message = "This user has an active Car"),403

        return jsonify(message = f"User disabled"),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500



@app.route("/user/reactive/<int:id>",methods = ["PATCH"])
@login_required
@admin_required
def reactive_user(id):
    try:
        user = user_repo.reactive_user(id)

        if user is False:
            return jsonify(message = "User not found"),404
        
        if user is None:
            return jsonify(message = "User is already active"),409

        return jsonify(message = "User reactive"),200
    except Exception as ex:
        return jsonify(message = str(ex)),500



#===============================================================================================================================
#                                                       CATEGORY ENDPOINTS
#===============================================================================================================================


@app.route("/category",methods = ["POST"])
@login_required
@admin_required
def create_category():
    try:
        if not request.json or not request.json["name"]:
            return jsonify(message = "Name is missing"),400

        category = category_repo.create_category(
            name=request.json["name"],
            description=request.json.get("description")
        )
        if not category:
            return jsonify(message = "Category already exist"),409

        cache_manager.delete_data("category:all")
        return jsonify(message = "Category created"),201

    
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/category/<int:id>",methods = ["PATCH"])
@login_required
@admin_required
def edit_category_flask(id):
    try:
        if not request.json or not request.json["name"]:
            return jsonify(message = "Name is missing"),400

        category = category_repo.edit_category(
            id=id,
            name=request.json["name"],
            description=request.json.get("description"),
            
        )
        if category is False:
            return jsonify(message = "Category not found"),404
        if category is None:
            return jsonify(message = "Category name already exist"),409


        cache_manager.delete_data("category:all")
        cache_manager.delete_data(f"category:{id}")
        return jsonify(message = "Category edited"),200

    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/category/<int:id>",methods = ["DELETE"])
@login_required
@admin_required
def delete_category_flask(id):
    try:
        category = category_repo.delete_category(id)
        if category is False:
            return jsonify(message = "Category not found"),404
        if category is None:
            return jsonify(message = "Category has items, cannot be deleted"),409

        
        cache_manager.delete_data("category:all")
        cache_manager.delete_data(f"category:{id}")
        return jsonify(message = "Category deleted"),200
        
    except Exception as ex:
            return jsonify(message = str(ex)),500




@app.route("/category/search", methods = ["GET"])
@login_required
def get_cate_by_name():
    try:
        
        valid = request.args.get("name")
        if not valid:
            return jsonify(message = "Name is missing"),400


        cate = category_repo.get_categories_by_name(valid)
        if not cate:
            return jsonify(message = "Category not found"),404

        return jsonify(
            name = cate.name,
            description = cate.description
        ),200
    
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/category", methods = ["GET"])
@login_required
def get_all_categories():
    try:

        key = "category:all"
        exist , tll = cache_manager.check_key(key)

        if exist:
            cached = cache_manager.get_data(key)
            return jsonify(json.loads(cached)),200

        cate = category_repo.get_all()
        if cate is None:
            return jsonify(message = "Not category created yet"),404

        list_ = []
        for l in cate:
            list_.append({
                "id" : l.id,
                "name" : l.name,
                "description" : l.description
            })
        cache_manager.store_data_redis(key,json.dumps(list_))
        return jsonify(list_),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/category/id/<int:id>",methods = ["GET"])
@login_required
def get_cate_by_id_flask(id):
    try:

        key = f"category:{id}"
        exist , tll = cache_manager.check_key(key)
        if exist:
            cached = cache_manager.get_data(key)
            return jsonify(json.loads(cached)), 200
        

        cate = category_repo.get_by_id(id)
        if not cate:
            return jsonify(message = "Category not found"),404

        cache_manager.store_data_redis(key, json.dumps(cate))
        return jsonify(cate),200
    except Exception as ex:
        return jsonify(message = str(ex)),500





#===============================================================================================================================
#                                                       ITEM ENDPOINTS
#===============================================================================================================================




@app.route("/item",methods =["POST"])
@login_required
@admin_required
def post_item():
    try:
        valid = ["name", "category_id", "stock", "price"]
        for v in valid:
            if v not in request.json or request.json[v] is None:
                return jsonify(message = f"{v} is missing"),400

        item = item_repo.create_item(
            name = request.json["name"],
            category_id = request.json["category_id"],
            stock = request.json["stock"],
            price = request.json["price"],
            description= request.json.get("description")
            )
        if item is False:
            return jsonify(message = "Item name already exist"),409
        
        if item == "Price must be greater than 0":
            return jsonify(message ="Price must be greater than 0"),400

        if item == "Stock cannot be negative":
            return jsonify(message = "Stock cannot be negative"),400
        
        if item is None:
            return jsonify(message = "Category does not exist"),404

        cache_manager.delete_data("item:all")
        return jsonify(message = "Item created"),201
    
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/item/<int:id>",methods = ["PATCH"])
@login_required
@admin_required
def edit_item_flask(id):
    try:
        valid = ["name","category_id","stock","price"]
        for v in valid:
            if v not in request.json or request.json[v] is None:
                return jsonify(message = f"{v} is missing"),400

        item = item_repo.edit_item(
            id=id,
            name = request.json["name"],
            category_id = request.json["category_id"],
            stock = request.json["stock"],
            price = request.json["price"],
            description= request.json.get("description")
        )
        if item is False:
            return jsonify(message = "Item not found"),404

        if item == "Price must be greater than 0":
            return jsonify(message ="Price must be greater than 0"),400
        
        if item == "Stock cannot be negative":
            return jsonify(message = "Stock cannot be negative"),400
        
        elif item is None:
            return jsonify(message = "Item name already exist"),409
        
        elif item == "Category does not exist":
            return jsonify(message = "Category does not exist"),404
        

    
        cache_manager.delete_data("item:all")
        return jsonify(message = "Item edited"),200

    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500   
    



@app.route("/item/<int:id>",methods = ["DELETE"])
@login_required
@admin_required
def deactivate_item_flask(id):
    try:
        item = item_repo.delete_item(id)
        if item is False:
            return jsonify(message = "Item not found"),404

        if item is None:
            return jsonify(message = "Cart with this item, you cant delete it"),409

        
        cache_manager.delete_data("item:all")
        return jsonify(message = "Item deactivated"),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500 




@app.route("/item/<int:id>/reactivate", methods=["PATCH"])
@login_required
@admin_required
def reactivate_item_flask(id):
    try:
        item = item_repo.reactivate_item(id)
        if item is False:
            return jsonify(message="Item not found"), 404
        if item is None:
            return jsonify(message="Item is already active"), 409

        if item == "no_category":
            return jsonify(message="This item's category no longer exists, assign a new category before reactivating"), 409

        cache_manager.delete_data("item:all")
        return jsonify(message="Item reactivated"), 200

    except Exception as ex:
        return jsonify(message=str(ex)), 500




@app.route("/item",methods = ["GET"])
@login_required
def get_all_items_flask():
    try:
        key ="item:all"
        exists, ttl = cache_manager.check_key(key)

        if exists:
            cached = cache_manager.get_data(key)
            return jsonify(json.loads(cached)), 200

        item = item_repo.get_all_items()
        if not item:
            return jsonify(message = "Items not found"),404

        cache_manager.store_data_redis(key, json.dumps(item))
        return jsonify(item),200
    except Exception as ex:
        return jsonify(message = str(ex)),500  




@app.route("/item/name", methods = ["GET"])
@login_required
def get_by_name_flask():
    try:
        valid = request.args.get("name")
        if not valid:
            return jsonify (message = "Name is missing"),400
        
        item = item_repo.get_by_name(valid)
        if not item:
            return jsonify(message = "Item name not fund"),404

        return jsonify(item),200
    except Exception as ex:
        return jsonify(message = str(ex)),500 




#===============================================================================================================================
#                                                        ADDRESS ENDPOINTS
#===============================================================================================================================




@app.route("/address",methods = ["POST"])
@login_required
def add_address_flask():
    try:
        valid = ["address"]
        for v in valid:
            if v not in request.json or not request.json[v]:
                return jsonify(message = f"{v} is missing"),400

        user = request.user["user_id"]
        address = address_repo.add_address(
            user_id = user,
            address = request.json["address"]
        )
        if address is False:
            return jsonify(message = "User id not found"),404
        if address is None:
            return jsonify(message = "User added this address already"),409
        return jsonify(message = "Address added"),201
    
    except ValueError as ex:
        return jsonify(message = str(ex)),500 
    except Exception as ex:
        return jsonify(message = str(ex)),500 




@app.route("/address/<int:id>",methods = ["DELETE"])
@login_required
def delete_address_flask(id):
    try:
        user = request.user["user_id"]
        address = address_repo.delete_address(id,user)
        if not address:
            return jsonify(message = "Address not found"),404
        return jsonify(message = "Address deleted"),200
    except Exception as ex:
        return jsonify(message = str(ex)),500





#===============================================================================================================================
#                                                       PAY METHOD ENDPOINTS
#===============================================================================================================================




@app.route("/pay_method", methods = ["POST"])
@login_required
def add_pay_method_flask():
    try:
        valid = ["pay_method"]
        for v in valid:
            if v not in request.json or not request.json[v]:
                return jsonify(message = f"{v} is missing"),400

        method = ["SINPE", "PAY TERMINAL", "TRANSACTION", "CASH"]
        if request.json["pay_method"] not in method:
            return jsonify(message = "Invalid method"),400

        user = request.user["user_id"]
        meth = pay_repo.add_pay_method(
            user_id = user,
            pay_method= request.json["pay_method"]
        )
        if meth is False:
            return jsonify(message = "User not found"),404
        if meth is None:
            return jsonify(message = "This pay method already exist"),409

        return jsonify(message = "Pay method added"),201
    
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/pay_method/<int:id>",methods = ["DELETE"])
@login_required
def delete_pay_method_flask(id):
    try:

        user = request.user["user_id"]
        meth = pay_repo.delete_method(id,user)
        if not meth:
            return jsonify(message = "Pay method not found"),404
        return jsonify(message = "Pay method deleted"),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500




#===============================================================================================================================
#                                                       CART/CART ITEM ENDPOINTS
#===============================================================================================================================




@app.route("/cart",methods = ["POST"])
@login_required
def cart_logic():
    try:
        valid  = ["item_id","quantity"]
        for v in valid:
            if v not in request.json or request.json[v] is None:
                return jsonify(message = F"{v} is missing"),400
            
        user = request.user["user_id"]
        cart = cart_repo.create_cart(user)
        if not cart:
            return jsonify(message = "Could not create"),400

        cart_item  = cart_repo.create_cart_item(
            cart_id=cart.id,
            item_id= request.json["item_id"],
            quantity=request.json["quantity"]
        )
        if cart_item is False:
            return jsonify(message = "Item not found"),404
        if cart_item is None:
            return jsonify(message = "Quantity must be grater than 0"),400
        if cart_item == "not_enough_stock":
            return jsonify(message = "Not enough stock"),400
        return jsonify(message = "Cart item created"),201
        
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/cart/<int:cart_id>/<int:item_id>",methods = ["PATCH"])
@login_required
def edit_cart_item_flask(cart_id,item_id):
    try:
        if "quantity" not in request.json or not request.json["quantity"]:
            return jsonify(message="quantity is missing"), 400

        user = request.user["user_id"]
        cart_item = cart_repo.edit_cart_item(
            user_id= user,
            cart_id= cart_id,
            item_id=item_id,
            quantity= request.json["quantity"]
        )
        if cart_item == "Cart does not belong to this user":
            return jsonify(message = "Cart does not belong to this user"),403
        if cart_item is False:
            return jsonify(message= "Item not found"),404
        if cart_item is None:
            return jsonify(message= "item is not in the cart"),404
        return jsonify(message= "item edited"),200
    
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/cart/<int:cart_id>/<int:item_id>", methods = ["DELETE"])
@login_required
def delete_cart_item_flask(cart_id,item_id):
    try:
        user = request.user["user_id"]
        cart_item = cart_repo.delete_cart_item(user,cart_id,item_id)

        if cart_item == "Cart does not belong to this user":
            return jsonify(message = "Cart does not belong to this user"),403

        if cart_item is False:
            return jsonify(message= "Item not found"),404
        
        if cart_item is None:
            return jsonify(message= "Item not in the cart"),404
        return jsonify(message = "Item deleted"),200

    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/cart/<int:cart_id>", methods = ["GET"])
@login_required
def get_cart_items(cart_id):
    try:
        user = request.user["user_id"]
        cart_items = cart_repo.get_all_cart_items(user, cart_id)

        if cart_items == "Cart does not belong to this user":
            return jsonify(message = "Cart does not belong to this user"),403

        if not cart_items:
            return jsonify(message = "No items in the cart"),404
        return jsonify(cart_items),200
    
    except Exception as ex:
        return jsonify(message = str(ex)),500




#===============================================================================================================================
#                                                       ITEM/INVOICE ITEM ENDPOINTS
#===============================================================================================================================




@app.route("/invoice",methods = ["POST"])
@login_required
def invoice_logic():
    try:
        valid = ["address_id","pay_method_id"]
        for v in valid:
            if v not in request.json or not request.json[v]:
                return jsonify(message=f"{v} is missing"),400

        user = request.user["user_id"]
        invoice = invoice_repo.create_invoice(
            user_id = user,
            address_id = request.json["address_id"],
            pay_method_id = request.json["pay_method_id"],
            note = request.json.get("note")
        )
        if invoice == "User not found":
            return jsonify(message = "User not found found"),404
        
        if invoice == "User address not found":
            return jsonify(message = "Address does not belong to this user"),404
        
        if invoice == "Pay method not allow":
            return jsonify(message = "Pay method does not belong to this user"),403
        
        if invoice is False:
            return jsonify(message = "Cart not found"),404
        if invoice is None:
            return jsonify(message = "Empty cart"),404

        if isinstance(invoice, str) and invoice.startswith("Not enough stock"):
            return jsonify(message=invoice), 400

        return jsonify(message = "Invoice created"),201   
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
    
        return jsonify(message = str(ex)),500




@app.route("/invoice", methods = ["GET"])
@login_required
def get_my_invoices():
    try:
        user=request.user["user_id"]
        invoice = invoice_repo.get_my_invoices(user)
        if invoice is False:
            return jsonify(message="User not found"),404
        if invoice is None:
            return jsonify(message="Invoices not found"),404

        return jsonify(invoice),200        
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/invoice/all_users",methods = ["GET"])
@login_required
@admin_required
def get_all_invoices():
    try:
        invoice = invoice_repo.all_user_invoice()
        if invoice is False:
            return jsonify(message="Invoices not found"),404

        return jsonify(invoice),200      
    except Exception as ex:
        return jsonify(message = str(ex)),500




@app.route("/return", methods = ["POST"])
@login_required
@admin_required
def create_return():
    try:
        valid = ["invoice_item_id", "quantity"]
        for v in valid:
            if v not in request.json or not request.json[v]:
                return jsonify(message=f"{v} is missing"),400

        return_ = return_repo.create_return(
            invoice_item_id=request.json["invoice_item_id"],
            quantity=request.json["quantity"]
        )
        if return_ is False:
            return jsonify(message="Invoices not found"),404

        if return_ == "Invalid return quantity":
            return jsonify(message="Invalid return quantity"),400
        
        if return_  == "Return quantity exceeds available amount":
            return jsonify(message="Return quantity exceeds available amount"),400
        
        return jsonify(message = "Return created"),201
        
    except ValueError as ex:
        return jsonify(message = str(ex)),500
    except Exception as ex:
        return jsonify(message = str(ex)),500




#code
if __name__ == "__main__":
    app.run(host="localhost", debug=True)