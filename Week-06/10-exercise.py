def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for chart in text:
        if chart in vowels:
            count +=1
    return count


text = 'I love my girl and she will be my personal employee the rest of her miserable life'
result = count_vowels(text)

print(result)