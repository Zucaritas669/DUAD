def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total +=n
    return total

# result = sum_of_list([4, 6, 2, 29])
# print(result)


def reverse_text(text):
    return text [::-1]


def count_capital_letter(text):
    count_upper = 0
    count_lower = 0

    for data in text:
        if data.isupper():
            count_upper +=1 
        elif data.islower():
            count_lower +=1

    return count_upper,count_lower

