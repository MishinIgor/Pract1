pets= {} #Список с питомцами
w = 1
while w == 1:
    name = input('Введите имя питомца: ')
    pets[name] = {}
    pets[name]['Вид питомца'] = input('Вид питомца: ')
    vozrast = int(input('Количество полных лет: '))
    if vozrast > 5 and vozrast <= 20 or vozrast % 10 == 0 or vozrast % 10 >=5:
        pets[name]['Его возраст'] = str(vozrast)+' лет'
    elif vozrast % 10 == 1:
        pets[name]['Его возраст'] = str(vozrast)+' год'
    elif vozrast % 10 >1 and vozrast % 10 <5:
        pets[name]['Его возраст'] = str(vozrast)+' года'
    pets[name]['Имя владельца'] = input('Имя владельца: ')
    w = int(input('Если хотите ввести ещё питомца введите 1: '))
print(pets)
#https://github.com/MishinIgor/Pract1.git
#PR8.1
