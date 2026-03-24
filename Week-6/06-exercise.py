def word(text):
    word = text.split('-')
    ordered_words = sorted(word)
    result = '-'.join(ordered_words)

    return result

result = word('carrot-watermelon-apple')
print(result)