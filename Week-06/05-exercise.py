def count_capital_letter(text):
    count_upper = 0
    count_lower = 0

    for data in text:
        if data.isupper():
            count_upper +=1 
        elif data.islower():
            count_lower +=1

    return count_upper,count_lower

count_upper, count_lower = count_capital_letter("I love Nación Sushi!")
print(f'Capital letters {count_upper}')
print(f'Lower letters {count_lower}')