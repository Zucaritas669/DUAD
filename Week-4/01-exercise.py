name = input('Type your name: ')
last_name= input('type your last name: ')
age= int(input('How old are you?: '))
    
if(age <= 2):
    print('you are a baby')
elif(age<=9 ):
    print('you are a child')
elif(age<=12 ):
    print('you are a pre adolescent')
elif(age<=18 ):
    print('you are a teenager')
elif(age<=35 ):
    print('you are a young_adult')
elif(age<=59 ):
    print('you are a adult ')
else:
    print('you are a senior')