from DB.tables import PayMethod
from DB.tables import User
from sqlalchemy import func
from Repo.handle_session import handle_session

class PayMethodRepository():

    @handle_session
    def add_pay_method(self, user_id, pay_method, s=None):
        user = s.get(User,user_id)
        if not user:
            print("User not found")
            return False

        method = s.query(PayMethod).filter(func.lower(PayMethod.pay_method)==pay_method.lower(), PayMethod.user_id == user_id).first()
        if method:
            print("This pay method already exist")
            return None


        pay = PayMethod(
            user_id = user_id,
            pay_method = pay_method
        )
        s.add(pay)
        s.commit()
        return True



    @handle_session
    def delete_method(self, id, user_id, s=None):
        exist = s.query(PayMethod).filter(PayMethod.id==id, PayMethod.user_id==user_id).first()
        if not exist:
            print("Pay method not found")
            return False

        s.delete(exist)
        s.commit()
        return True
