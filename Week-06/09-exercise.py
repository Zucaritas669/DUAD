def bigger_than_number(words, n):
    new_list = []
    for word in words:
        if len(word) > n:
            new_list.append(word)
    return new_list


text = input("Type 3 words:\n-> ")
number = int(input("Type a number:\n-> "))

result = bigger_than_number(text, number)
print(result)