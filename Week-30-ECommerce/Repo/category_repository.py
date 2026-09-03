from DB.tables import Category,Item
from sqlalchemy import func
from Repo.handle_session import handle_session

class CategoryRepository():

    @handle_session
    def create_category(self, name, description=None, s=None):
        category = s.query(Category).filter(func.lower(Category.name) == name.lower()).first()
        if category:
            print("Category already exist")
            return False

        category = Category(
            name = name,
            description = description
        )
        s.add(category)
        s.commit()
        return True



    @handle_session
    def edit_category(self, id,name, description=None, s=None):
        category = s.get(Category,id)
        if not category:
            print("Category not found")
            return False

        category_name = s.query(Category).filter(func.lower(Category.name) == name.lower(), Category.id != id).first()
        if category_name:
            print("Category already exist")
            return None
        

        category.name = name
        category.description = description
        s.commit()
        return True



    @handle_session
    def delete_category(self, id, s=None):
        category = s.get(Category,id)
        if not category:
            print("Category not found")
            return False

        has_item = s.query(Item).filter(Item.category_id == id, Item.is_active ==True).first()
        if has_item:
            print("Category has items, cannot delete")
            return None

        s.delete(category)
        s.commit()
        return True



    @handle_session
    def get_categories_by_name(self, name, s=None):
        cate = s.query(Category).filter(func.lower(Category.name) == name.lower()).first()
        if not cate:
            print("Category does noy exist")
            return None
        
        return cate



    @handle_session
    def get_all(self, s=None):
        category = s.query(Category).all()
        if not category:
            print("Not category created yet")
            return None
        
        return category


    @handle_session
    def get_by_id(self,id, s=None):
        cate = s.get(Category,id)
        if not cate:
            print("Category not found")
            return False

        return ({
            "id":cate.id,
            "name":cate.name,
            "description":cate.description
        })
    
        