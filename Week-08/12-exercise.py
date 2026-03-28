import json

def menu():

    print('----Pokedex----')
    print('1-> Show up Pokemon')
    print('2-> Add Pokemon')
    print('3-> Search Pokemon ')
    print('4-> Average ')
    print('5-> EXIT')

def get_number():
    while True:
        try:
            number = int(input('\n---Select an option----\n->'))
            return number
        except  ValueError as ex:
            print(f'It must be number: {ex}')
            break


def load_pokemon(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        pokemon= json.load(file)
        

    for poke in pokemon:
        print(f'Name: {poke["name"]["english"]}')
        print(f'Type: {poke["type"]}')
        print(f'HP: {poke["base"]["HP"]}')
        print(f'Attack: {poke["base"]["Attack"]}')
        print(f'Defense: {poke["base"]["Defense"]}')
        print(f'SP Attack: {poke["base"]["Sp. Attack"]}')
        print(f'Sp Defense: {poke["base"]["Sp. Defense"]}')
        print(f'Speed: {poke["base"]["Speed"]}')
        print('-'*30)
    return pokemon
        

def add_pokemon(pokemon,file_path):

    while True:
        name = input('Pokemon name: ').strip()
        if name.isalpha():
            break
        else:
            print(f'{name} it must be letters only')

    types_dict = {
        1: "normal",
        2: "fire",
        3: "water",
        4: "grass",
        5: "electric",
        6: "ice",
        7: "fighting",
        8: "poison",
        9: "ground",
        10: "flying",
        11: "psychic",
        12: "bug",
        13: "rock",
        14: "ghost",
        15: "dragon",
        16: "dark",
        17: "steel",
        18: "fairy"
}
    
    for key, value in types_dict.items():
        print(f'{key}:{value}')

    while True:
        try:
            choice = int(input('Choose your pokemon type: '))
            type_ = types_dict[choice]
            break
        except (ValueError, KeyError) as ex:
            print(f'Invalid option {ex}')
    print(f'Selected type {type_} ')



    stats = {}
    for stats_name in ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]:
        while True:
            try:
                stats[stats_name] = int(input(f'{stats_name}'))
                break
            except ValueError as ex:
                print('It must be a number')


    new_poke = {
        "name": {
            "english": name
        },
        "type": [
            type_
        ],
        "base": stats
        
    }

    pokemon.append(new_poke)


    with open(file_path,'w',encoding='utf-8',) as file:
        json.dump(pokemon,file,indent=4,ensure_ascii=False)

    print('Pokemon added successfully')


def search_pokemon(pokemon):
    while True:   
        type_ = input('Search pokemon by Type: ').lower()

        if type_ == 'exit':
            break

        result = []
        for poke in pokemon:
            for t in poke["type"]:
                if t.lower() == type_:
                    result.append(poke)
        for p in result:
            print(f'{p["name"]["english"]}--[{p["type"]}]')


def group_and_average(pokemon_list):
    groups = {}
    
    for p in pokemon_list:
        for poke_type in p["type"]:
            if poke_type not in groups:
                groups[poke_type] = []
            total_stats = sum(p["base"].values())
            groups[poke_type].append(total_stats)
    
    for poke_type, stats in groups.items():
        print(f'{poke_type}: {sum(stats)/len(stats)}')

        


def main():
    file_path = "pokemon.json"

    while True:
        menu()
        option = get_number()

        if option == 1:
            load_pokemon(file_path)

        elif option == 2:
            result=load_pokemon(file_path) 
            add_pokemon(result,file_path)

        elif option == 3:
            result=load_pokemon(file_path) 
            search_pokemon(result)

        elif option == 4:
            result = load_pokemon(file_path)
            group_and_average(result)

        elif option == 0:
            print('Goodbye')
            break

        else:
            print('Invalid option')

main()