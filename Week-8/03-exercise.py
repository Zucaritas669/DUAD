def count_words(entry_file):
    count = 0
    with open(entry_file,'r',encoding='utf-8') as file:
        for line in file:

            words = line.split()
            count += len(words)
        
    return count

def main():
    file_count = 'entry.txt'
    result = count_words(file_count)
    print(f'The file has {result} letters')
        

main()