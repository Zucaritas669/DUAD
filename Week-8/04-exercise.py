def capital_letter(element_entry,element_exit):

    with open(element_entry,'r',encoding='utf-8') as file1:
        with open(element_exit,'w',encoding='utf-8') as file2:

            for line in file1:
                file2.write(line.upper())

def main():
    entry_file = 'entry.txt'
    exit_file = 'exit.txt'

    capital_letter(entry_file,exit_file)
    print('Done!!')

main()