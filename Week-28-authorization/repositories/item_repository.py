from db_tables import Item
from repositories.session import handle_session

class ItemRepository:

    @handle_session
    def create_item(self ,name, price, stock, s=None):
        
        item = Item(
            name= name, 
            price= price, 
            stock=stock
            )
        s.add(item)
        s.commit()
        return True 
    


    @handle_session
    def get_item_by_id(self, id, s=None):

        item = s.get(Item, id)
        if not item:
            print("Item not found")
            return False
        return item
    

    @handle_session
    def get_all_items(self,s=None):

        item = s.query(Item).all()
        return item
    

    @handle_session
    def edit_item(self, id, name, price, stock, s=None):
        item = s.get(Item, id)
        if not item:
            print("Item not found")
            return False
        
        item.name= name 
        item.price= price
        item.stock=stock
        s.commit()
        return True


    @handle_session
    def delete_item(self, id , s=None):
        item = s.get(Item, id)
        if not item:
            print("Item not found")
            return False
        
        s.delete(item)
        s.commit()
        return True
        


