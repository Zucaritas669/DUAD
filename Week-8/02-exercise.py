def read_file(jumps):
    with open(jumps,'r',encoding='utf-8') as file:
        return file.readlines()
    

def remove_newlines(text):
    return text.replace('\n',' ')
    

def write_file(new_file, text):
    with open(new_file,'w',encoding='utf-8') as file:
        file.write(text)
        

def main():
    results = read_file('saltos_de_linea.txt')

    text = ''.join(results)

    
    text_no_newlines = remove_newlines(text)

    
    write_file('sin_saltos.txt', text_no_newlines)

main()