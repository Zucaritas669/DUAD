from DB.tables import Return, InvoiceItem , Item
from Repo.handle_session import handle_session
from sqlalchemy import func


class ReturnRepository():

    @handle_session
    def create_return(self, invoice_item_id, quantity,  s=None):

        invoice_item = s.get(InvoiceItem, invoice_item_id)
        if not invoice_item:
            print("Invoice not found")
            return False

        if quantity <= 0:
            return "Invalid return quantity"

        # Suma todas las devoluciones previas de este mismo invoice_item,
        # para no permitir devolver más de lo que realmente se compró
        item_returned = s.query(func.sum(Return.quantity)).filter(Return.invoice_item_id == invoice_item.id).scalar()
        if item_returned is None:
            item_returned =0

        allow_to_return = invoice_item.amount - item_returned
        if quantity > allow_to_return:
            return "Return quantity exceeds available amount"
            

        total  = quantity *invoice_item.unit_price
        return_ = Return(
            invoice_item_id = invoice_item_id,
            quantity = quantity,
            total_returned = total
        )
        s.add(return_)
        invoice_item.item.stock += quantity
        s.commit()

        return return_






        

    

        
    