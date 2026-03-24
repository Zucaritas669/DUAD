def convert_to_int(list1):
    new_list = []

    for index in list1:
        try:
            num = int(index)
            new_list.append(num)

        except ValueError:
            print(f'I cant convert the element: {index}')

    return new_list


element = ["10", "20", "hola", "30", "5.5", "40"]
result = convert_to_int(element)

print("Original list:", element)
print("Converted list:", result)