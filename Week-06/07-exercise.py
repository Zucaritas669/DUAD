def prime_number(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_list(list):
    prime = []
    for n in list:
        if prime_number(n):
            prime.append(n)

    return(prime)
    
n= [1, 4, 6, 7, 13, 9, 67]
result = prime_list(n)
print(result)
