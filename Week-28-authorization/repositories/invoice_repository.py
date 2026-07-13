from db_tables import Invoice, Item, InvoiceItem
from repositories.session import handle_session

class InvoiceRepository():

    @handle_session
    def create_purchase(self, user_id, items, s=None):
        
        invoice = Invoice(
            user_id = user_id,
            total = 0,
        )
        total = 0

        for buy in items:
            get_item = s.get(Item, buy["item_id"])
            if not get_item or get_item.stock < buy["quantity"]:
                raise ValueError(f"Invalid purchase for item {buy['item_id']}")

            sub_total = get_item.price * buy["quantity"]
            total += sub_total
            get_item.stock -= buy["quantity"]

            invoice.invoice_items.append(InvoiceItem(
                item_id = get_item.id,
                quantity=buy["quantity"],
                unit_price=get_item.price,
                sub_total=sub_total
            ))
        invoice.total = total
        s.add(invoice)
        s.commit()
        return invoice
    

    @handle_session
    def get_invoices(self, user_id, s=None):
        invoice_ = s.query(Invoice).filter(Invoice.user_id == user_id).all()
        if not invoice_:
            print("This user does not have invoices")
            return False
        
        return invoice_


    @handle_session
    def get_all_invoices(self, s=None):
        get_all = s.query(Invoice).all()
        return get_all