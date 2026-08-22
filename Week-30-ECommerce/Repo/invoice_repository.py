from DB.tables import User, Address, PayMethod,Cart,CartItem, Invoice, Item , InvoiceItem
from Repo.handle_session import handle_session

class InvoiceRepository():

    @handle_session
    def create_invoice(self, user_id, address_id, pay_method_id, total=0, note=None, s=None):

        user = s.get(User,user_id)
        if not user:
            return "User not found"
        
        address = s.query(Address).filter(Address.user_id == user_id, Address.id == address_id).first()
        if not address:
            return "User address not found"
        
        pay = s.query(PayMethod).filter(PayMethod.user_id == user_id, PayMethod.id == pay_method_id).first()
        if not pay:
            return "Pay method not allow"



        has_user_cart = s.query(Cart).filter(Cart.user_id==user_id, Cart.status == "active").first()
        if not has_user_cart:
            print("Not cart found")
            return False
        get_cart_items = s.query(CartItem).filter(CartItem.cart_id == has_user_cart.id).all()
        if not get_cart_items:
            print("Empty cart")
            return None

        for cart_item in get_cart_items:
            item = cart_item.item

            if item.is_active == False:
                return f"Item {item.name} is no longer available"
            if item.stock < cart_item.quantity:
                return f"Not enough stock for {item.name}"
            


        invoice = Invoice(
            user_id = user_id,
            address_id = address_id,
            pay_method_id = pay_method_id,
            total = total,
            note = note
        )
        s.add(invoice)
        s.commit()
        s.refresh(invoice)

        total_balance = 0
        for cart_item in get_cart_items:
            item = cart_item.item
            sub_total = cart_item.quantity * item.price
            total_balance += sub_total

            invoice_item = InvoiceItem(
                invoice_id = invoice.id,
                item_id = item.id,
                amount = cart_item.quantity,
                unit_price = item.price,
                sub_total = sub_total,
                note = note
            )
            s.add(invoice_item)
            item.stock -= cart_item.quantity
            s.delete(cart_item)

            
            
        invoice.total = total_balance
        has_user_cart.status = "completed"
        s.commit()
        return invoice



    @handle_session
    def get_my_invoices(self, user_id, s=None):
        user = s.get(User,user_id)
        if not user:
            print("User not found")
            return False

        invoices = s.query(Invoice).filter( Invoice.user_id == user.id).all()
        if not invoices:
            print("Invoices not found")
            return None

        list_ = []
        for i in invoices:
            list_.append({
            "invoice_id": i.id,
            "Name" : i.user.name,
            "Email" : i.user.email,
            "address": i.address.address,
            "pay_method": i.pay_method.pay_method,
            "total": i.total,
            "note": i.note,
            "created_at": i.created_at
            })

        return(list_)



    @handle_session
    def all_user_invoice(self,s=None):
        invoices = s.query(Invoice).all()
        if not invoices:
            print("Not invoices created yet")
            return False

        list_ = []
        for i in invoices:
            list_.append({
            "invoice_id": i.id,
            "Name" : i.user.name,
            "Email" : i.user.email,
            "address": i.address.address,
            "pay_method": i.pay_method.pay_method,
            "total": i.total,
            "note": i.note,
            "created_at": i.created_at
            })

        return list_
