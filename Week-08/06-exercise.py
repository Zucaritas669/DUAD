import csv

def get_number():
    while True:
        try:
            n = int(input('---How many games do you want to add?---\n->'))
            if n <= 0:
                print('\nInvalid option')
                
            else:
                return n
        except ValueError as ex:
            print(f'\nOnly numbers pleas!!!! {ex}')


def get_text(data):
    while True:
        text = input(data)
        if text.replace(' ', '').isalpha():
            return text
        else:
            print('\nError, only letters allowed') 


def get_games():
    games_list = []
    games = get_number()
    
    while (len(games_list)<games):

        print(f'\nGame #{len(games_list)+1}')

        name = get_text('Name:')
        genre = get_text('Genre:')
        developer = get_text('Developer:')
        esrb = get_text('ESRB:')

        games_list.append({
            'name':name,
            'genre':genre,
            'developer':developer,
            'esrb':esrb
        })

    return games_list


#---------Write CSV---------

def write_games(file_path,data):

    headers = [
        'name',
        'genre',
        'developer',
        'esrb'
    ]

    with open(file_path,'w',encoding='utf-8',newline='') as file:
        write = csv.DictWriter(file,headers)
        write.writeheader()
        write.writerows(data)


def main():
    games = get_games()
    write_games('games.csv',games)
    print('CSV created successfully!!')


main()