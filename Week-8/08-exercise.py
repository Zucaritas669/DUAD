import csv


def read_file(file_path):

    with open(file_path,'r',encoding='utf-8') as file:
        read = csv.reader(file)
        next(read)

        for row in read:
            print(F'Name: {row[0]}')
            print(f'Genre: {row[1]}')
            print(f'Developer: {row[2]}')
            print(f'ESRB: {row[3]}')
            print('-' * 30)

def main(): 
    read_file('games.csv')
    

main()