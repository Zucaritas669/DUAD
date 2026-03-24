men = 0
women = 0
counter = 1 
average_women = 0
average_men = 0

list_of_sex = []

for i in range(6):
    sex = int(input('type 1 for women or 2 for men: '))
    list_of_sex.append(sex)
    print(list_of_sex)

women =list_of_sex.count(1)
men =list_of_sex.count(2)

average_women = (women/6)*100
average_men = (men/6)*100



print(f'Average men {average_men}')
print(f'Average women {average_women}')