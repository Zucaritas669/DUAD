sales = [
    {
        'date': '01/01/24',
        'customer_email': 'shalston@gmail.com', 
        'items':[
            {'name':'Mouse','upc':'ITEM-1','unit_price': 10},
            {'name': 'Keyboard', 'upc': 'ITEM-2', 'unit_price': 20},           
        ]
    },
    {
                'date': '01/01/24',
        'customer_email': 'fiorella@gmail.com', 
        'items':[
            {'name':'Mouse','upc':'ITEM-1','unit_price': 10},
        ]
    }
]


result={}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']

        if upc in result:
            result[upc] += price
        else:
            result[upc] = price

print(result)