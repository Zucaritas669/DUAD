def add_file():
    line = input("type something: ")

    with open('entry.txt', 'a', encoding='utf-8') as file:
        file.write(line.strip() + "\n")

    print('=== Done!! ===')