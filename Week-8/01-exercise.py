def read_file(songs_file):
    with open(songs_file,'r',encoding='utf-8') as file1:
        result_read_file = file1.readlines()
    return result_read_file
    
def sorted_file(sorted_songs_file,lines):
    with open(sorted_songs_file,'w',encoding='utf-8') as file2:
        for line in lines:
            file2.write(line)

    
def main():
    result_1 = read_file('entry.txt')
    print('\n===Entry file===\n')
    for line in result_1:
        print(line.strip())
        
    
    result_1.sort()
    sorted_file('exit.txt',result_1)
    print('\n===Exit File===\n')
    for line in result_1:
        print(line.strip())

main()