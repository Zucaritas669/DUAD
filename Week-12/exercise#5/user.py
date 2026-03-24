from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    @abstractmethod
    def has_permission(self,permission):
        pass


class AdminUser(User):
    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True
    

class RegularUser(User):
    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        return permission == "read"
    


admin = AdminUser()
regular = RegularUser()

print(admin.get_role())
print(admin.has_permission("delete"))

print(regular.get_role())
print(regular.has_permission("read"))   
print(regular.has_permission("delete"))