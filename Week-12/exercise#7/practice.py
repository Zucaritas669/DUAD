def get_int(prompt):
    while  True:
        try:
            int_ = int(input(prompt))
            if int_ < 0:
                print("Invalid Format")
            else:
                return int_
        except ValueError as ex:
            print(ex)

def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text.replace(" ","").isalpha():
            return text
        else:
            print("Invalid Format")

def get_cc(prompt):
    while True:
        text = input(prompt).strip()
        if text.replace(" ",""):
            return text
        else:
            print("Invalid Format")


class Payment():
    def __init__(self,amount):
        self.amount = amount
        self.currency = "USD"

    def process(self):
        print(f"Processing payment of {self.amount}{self.currency}")

    def show_info(self):
        print("-"*30)
        print(f"Amount: {self.amount} || Currency: {self.currency}")
    


class CreditCardPayment(Payment):
    def __init__(self, amount,card_number):
        super().__init__(amount)
        self.card_number = card_number[-4:]

    def process(self):
        super().process()
        print(f"with card ending in {self.card_number}")

    def show_info(self):
        super().show_info()
        
        print(f"|| Card Info: {self.card_number}")


class CryptoPayment(Payment):
    def __init__(self, amount,wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address

    def process(self):
        super().process()
        print(f"Processing crypto payment of {self.amount} {self.currency} to wallet {self. wallet_address}")

    def show_info(self):
        super().show_info()
        print(f"|| Wallet address: {self.wallet_address}")


def get_payment():
    print()
    print("---------- Payment ------------")
    return Payment(get_int("Amount -> "))

def get_ccp():
    print()
    print("---------- Credit Card Payment  ------------")
    return CreditCardPayment(get_int("Amount -> "), get_cc("Card number -> "))

def get_cp():
    print()
    print("---------- Crypto  Payment  ------------")
    return CryptoPayment(get_int("Amount -> "), get_int("Wallet address -> "))



p = get_payment()

p.process()
p.show_info()

ccp = get_ccp()
ccp.process()
ccp.show_info()

cp = get_cp()
cp.process()
cp.show_info()