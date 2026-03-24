def count_characters(text,character):
    count = 0
    for letter in text:
        if letter == character:
            count +=1
    return count

text = input('Type your text\n->')
character = input('Target character\n->')

result = count_characters(text, character)

print (f'The chart appears {result} times' )