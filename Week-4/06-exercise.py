final_price = 0
price = int(input('What is the price of the product?? '))

if(price < 100):
    final_price = price * 0.98
    print(f"The final price is {final_price} ")

else:
    final_price = price * 0.90
    print(f"The final price is {final_price} ")