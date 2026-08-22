from DB.tables import Address,User
from Repo.handle_session import handle_session

from sqlalchemy import func

class AddressRepository():

    @handle_session
    def add_address(self, user_id, address, s=None):

        user = s.get(User,user_id)
        if not user:
            print("User not found")
            return False

        adr = s.query(Address).filter(func.lower(Address.address)== address.lower(), Address.user_id == user_id).first()
        if adr:
            print("User added this address already")
            return None

        direction = Address(
            user_id = user_id,
            address = address
        )
        s.add(direction)
        s.commit()
        return True



    @handle_session
    def delete_address(self, id, user_id, s=None):
        adr = s.query(Address).filter(Address.user_id==user_id, Address.id==id).first()
        if not adr:
            print("Address not found")
            return False

        s.delete(adr)
        s.commit()
        return True
