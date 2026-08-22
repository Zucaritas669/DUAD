from DB.tables import Item,Category,CartItem
from sqlalchemy import func

from Repo.handle_session import handle_session

class ItemRepository():

    @handle_session
    def create_item(self, name, category_id, stock, price, description=None, s=None):

        if price <= 0:
            return "Price must be greater than 0"

        if stock <= 0:
            return "Stock cannot be negative"

        exist = s.query(Item).filter(func.lower(Item.name)==name.lower(), Item.is_active == True).first()
        if exist:
            print("Item name already exist")
            return False

        item_category = s.get(Category,category_id)
        if not item_category:
            print("Category doest exist")
            return None
        

        exist = Item(
            name=name,
            category_id = category_id,
            stock = stock,
            price = price,
            description = description
        )
        s.add(exist)
        s.commit()
        return True



    @handle_session
    def edit_item(self, id, name, category_id, stock, price, description=None, s=None):


        if price <= 0:
            return "Price must be greater than 0"

        if stock <= 0:
            return "Stock cannot be negative"

        item = s.get(Item,id)
        if not item:
            print("item not found")
            return False

        item_name = s.query(Item).filter(func.lower(Item.name)==name.lower(), Item.id != id, Item.is_active == True).first()
        if item_name:
            print("Item name already exist")
            return None

        category = s.get(Category,category_id)
        if not category:
            return "Category does not exist"

        
        item.name = name
        item.category_id = category_id
        item.stock = stock
        item.price = price
        item.description = description
        s.commit()
        return True


    @handle_session
    def delete_item(self, id, s=None):
        item = s.get(Item,id)
        if not item:
            print("Item not found")
            return False   

        has_cart_item = s.query(CartItem).filter(CartItem.item_id == id).first()
        if has_cart_item:
            print("There is a Cart with this Item, you can not delete it")
            return None

        
        item.is_active = False
        s.commit()
        return True


    @handle_session
    def reactivate_item(self, id, s=None):
        item = s.get(Item, id)
        if not item:
            print("Item not found")
            return False

        if item.is_active:
            print("Item is already active")
            return None

        category = s.get(Category,item.category_id)
        if not category:
            return "no_category"

        item.is_active = True
        s.commit()
        return True


    @handle_session
    def get_all_items(self, s=None):
        item = s.query(Item).filter(Item.is_active == True).all()
        if not item:
            print("Items not found")
            return False

        items_list = []
        for i in item:
            items_list.append({
            "id" : i.id,
            "name" : i.name,
            "category" : i.category.name,
            "stock" : i.stock,
            "price" : i.price,
            "description" : i.description
        })
        return items_list




    @handle_session
    def get_by_name(self, name, s=None):
        item = s.query(Item).filter(func.lower(Item.name)== name.lower(),Item.is_active == True).first()
        if not item:
            print("Item not found")
            return False

        return ({
            "id" : item.id,
            "name" : item.name,
            "category" : item.category.name,
            "stock" : item.stock,
            "price" : item.price,
            "description" : item.description
        })


    # Create a get by category_name or id


    
    
        

        
        

        
