def show_menu():
    print("")
    print('='*30)
    print("     Student menu     ")
    print('='*30)
    print("1 ➬ Add student")
    print("2 ➬ Show students information")
    print("3 ➬ Get top 3 averages")
    print("4 ➬ Get average from the averages")
    print("5 ➬ Export to CSV")
    print("6 ➬ Import from CSV")
    print("7 ➬ Show failed students")
    print("8 ➬ Delete student")
    print("9 ➬ EXIT")
    print()


def get_option():

    option_list = range(1,10)

    while True:
        try:
            number = int(input("Select an option ➾ "))
            if number in option_list:
                break
            else:
                print("\n⚠︎ Invalid option ⚠︎ ")
                
        except ValueError as ex:
            print(f"\n⚠︎ Invalid option ⚠︎ \n{ex} ")
    return number
                



    