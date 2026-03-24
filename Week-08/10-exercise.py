import csv


def lookup_file(file_path):
        genre_count = {}
        
        with open(file_path,'r',encoding='utf-8') as file:
            read = csv.reader(file)
            next(read)

            for row in read:
                genre = row[1]
                
                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1
        return genre_count


def main(): 
    result = lookup_file('games.csv')

    print('Games by genre\n')
    for genre in sorted(result):
        print(f'{genre}: {result[genre]}')


main()