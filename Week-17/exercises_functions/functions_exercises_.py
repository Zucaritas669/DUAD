#-------------------- 1----------------------

def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


#-------------------- 2----------------------

def reverse_text(text):
    return text[::-1]


#-------------------- 3 ----------------------

def count_capital_letter(text):
    count_upper = 0
    count_lower = 0

    for data in text:
        if data.isupper():
            count_upper += 1
        elif data.islower():
            count_lower += 1

    return count_upper, count_lower


#-------------------- 4----------------------

def sort_hyphenated_string(text):
    word = text.split('-')
    ordered_words = sorted(word)
    result = '-'.join(ordered_words)
    return result


#-------------------- 5 ----------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    prime = []
    for n in numbers:
        if is_prime(n):
            prime.append(n)
    return prime


    
