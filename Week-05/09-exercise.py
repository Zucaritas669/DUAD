['estrella', 'planeta']

list_1 = []

for i in range(5):
    word = str(input(f'Type 5 random word\nword number {i +1} ---> : '))
    list_1.append(word)
    print(list_1)

words_list =[]
for word in list_1:
    if len(word) > 4:
        words_list.append(word)

print(f'Original list {list_1}')
print(f'Words with 4 or more characters {words_list}')