from DB.tables import Cart, CartItem, Item, User
from sqlalchemy import func
from Repo.handle_session import handle_session
from sqlalchemy.orm import joinedload
class CartRepository():

    @handle_session
    def create_cart(self, user_id, status="active" , s=None):


        cart_exist = s.query(Cart).filter(Cart.user_id == user_id, Cart.status == "active").first()
        if cart_exist:
            print("Cart already exist")

        else:
            cart_exist = Cart(
                user_id=user_id,
                status=status
            )
            s.add(cart_exist)
            s.commit()
            s.refresh(cart_exist)
        return cart_exist
    



    @handle_session
    def create_cart_item(self, cart_id, item_id, quantity, s=None):

        item = s.query(Item).filter(Item.id == item_id, Item.is_active ==True).first()
        if not item:
            print("Item not found")
            return False

        if quantity <= 0:
            print("Quantity must be grater than 0")
            return None


        is_item_in = s.query(CartItem).filter(CartItem.cart_id== cart_id, CartItem.item_id==item_id).first()
        if is_item_in:
            new_quantity = is_item_in.quantity + quantity
            if new_quantity > item.stock:
                return "not_enough_stock"
            
            is_item_in.quantity = new_quantity
            s.commit()
            return is_item_in


        else:
            if quantity > item.stock:
                return "not_enough_stock"

            cart_item = CartItem(
                cart_id = cart_id,
                item_id= item_id,
                quantity = quantity
            )
            s.add(cart_item)
            s.commit()
            s.refresh(cart_item)
            return cart_item



    @handle_session
    def edit_cart_item(self, user_id,cart_id, item_id, quantity, s=None):

        user = s.query(Cart).filter(Cart.id==cart_id, Cart.user_id==user_id).first()
        if not user:
            return "Cart does not belong to this user"

    
        item = s.query(Item).filter(Item.id == item_id, Item.is_active ==True).first()
        if not item:
            print("Item not found")
            return False

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return None

        #Verifica si ese producto específico ya está agregado a ese carrito específico
        cart_item = s.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.item_id==item_id).first()
        if not cart_item:
            print("Item is not in the cart")
            return "not_in_cart"

        if quantity > item.stock:
            return "not_enough_stock"

        cart_item.quantity = quantity
        s.commit()
        s.refresh(cart_item)
        return cart_item


    

    #borra item del cart no el cart item
    @handle_session 
    def delete_cart_item(self, user_id, cart_id, item_id, s=None):

        user = s.query(Cart).filter(Cart.id==cart_id, Cart.user_id==user_id).first()
        if not user:
            return "Cart does not belong to this user"
        

        item = s.get(Item,item_id)
        if not item:
            print("Item not found")
            return False

        cart_item = s.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.item_id==item_id).first()
        if not cart_item:
            print("Item not in the cart")
            return None

        s.delete(cart_item)
        s.commit()
        return True


    @handle_session
    def get_all_cart_items(self, user_id, cart_id, s=None):

        user = s.query(Cart).filter(Cart.id==cart_id, Cart.user_id==user_id).first()
        if not user:
            return "Cart does not belong to this user"
                

        cart_item = s.query(CartItem).options(joinedload(CartItem.item)).filter(CartItem.cart_id==cart_id).all()
        if not cart_item:
            print("No items in the cart ")
            return False

        list_= []
        for c in cart_item:
            list_.append({
                "Item name" : c.item.name,
                "Item price" : float(c.item.price),
                "Quantity" : c.quantity,
            })
        return (list_)



    @handle_session
    def get_active_cart(self, user_id, s=None):
        cart = s.query(Cart).filter(Cart.user_id == user_id, Cart.status == "active").first()
        if not cart:
            print("No active cart found")
            return False

        cart_items = s.query(CartItem).options(joinedload(CartItem.item)).filter(CartItem.cart_id == cart.id).all()

        items_list = []
        for c in cart_items:
            items_list.append({
                "item_id": c.item.id,
                "item_name": c.item.name,
                "item_price": float(c.item.price),
                "quantity": c.quantity
            })

        return {
            "cart_id": cart.id,
            "status": cart.status,
            "items": items_list
        }




        



    


    




        




