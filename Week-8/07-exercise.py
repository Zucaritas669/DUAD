import csv
def get_number():
    while True:
        try:
            n = int(input('How many games do you want to add?\n->  '))
            return n
        except ValueError as ex:
            print(f'Error: {ex}') 


def get_text(data):
    while True:
        text = input(data)
        if text.isalpha():
            return text
        else:
            print('ERROR: Only letters allowed')

        

def get_games():
    new_list =[]
    n = get_number()

    while len(new_list) < n:
            print(f'Game#{len(new_list)+1}')
            name = get_text('Game name:')
            genre = get_text('Genre: ')
            developer = get_text('Developer: ')
            esrb = get_text('Esrb: ')

            new_list.append({
                'name':name,
                'genre':genre,
                'developer':developer,
                'esrb':esrb
            })

    return new_list



# -------- WRITE CSV --------

def write_games(file_path,data):
    headers =[
        'name',
        'genre',
        'developer',
        'esrb'
    ]

    with open(file_path,'w',encoding='utf-8') as file:
        write = csv.DictWriter(file,headers,delimiter='\t')
        write.writeheader()
        write.writerows(data)


def main():
    games = get_games()
    write_games('games.tsv',games)
    print('TSV created successfully!!')


main()