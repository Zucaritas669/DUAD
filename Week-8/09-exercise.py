import csv


def lookup_file(file_path):
        while True:
            search  = input('Search games by ESRB\n-> ').upper()
            if not search.isalpha():
                print('Invalid option')
            
            with open(file_path,'r',encoding='utf-8') as file:
                read = csv.reader(file)
                next(read)

                for row in read:
                    if row[3].upper() == search:
                        print(F'Name: {row[0]}')
                        print(f'Genre: {row[1]}')
                        print(f'Developer: {row[2]}')
                        print(f'ESRB: {row[3]}')
                        print('-' * 30)
    

def main(): 
    lookup_file('games.csv')
    

main()