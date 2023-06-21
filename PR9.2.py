import collections
pets = {}
uslovie = ''

def get_suffix(age): #Функция для правильного описания возраста
    if age > 5 and age <= 20 or age % 10 == 0 or age % 10 >=5:
        nage = str(age)+' лет'
    elif age % 10 == 1:
        nage = str(age)+' год'
    elif age % 10 >1 and age % 10 <5:
        nage = str(age)+' года'
    return nage

def create(): #Функция создаёт нового питомца
    if len(pets) == 0:
        last = 0
    else:
        last = collections.deque(pets, maxlen=1)[0]
    name = input('Введите имя питомца: ')
    last+=1
    pets[last] = {
        name: {
        'Вид питомца: ': input('Введите вид питомца: '),
        'Возраст питомца: ': get_suffix(int(input('Введите количество полных лет: '))),
        'Имя владельца: ': input('Введите имя владельца: ')
        }
    }
    return last

def pets_list(): #Функция вывода списка имён питомцев
    for value in pets.values():
        for i in value.keys():
            print(i, sep=',', end = ' ')
    print()

def update():
    a = input('Введите имя питомца, информацию о котором нужно обновить: ')
    for key, value in pets.items():
        if a in value.keys():
            pets[key][a]['Вид питомца'] = input('Введите вид питомца: ')
            pets[key][a]['Возраст питомца'] = get_suffix(int(input('Введите количество полных лет: ')))
            pets[key][a]['Имя владельца'] = input('Имя владельца: ')
    else:
        print('Питомец не найден')

def read():
    a = input('Введите имя питомца, информацию о котором нужно получить: ')
    for key, value in pets.items():
        if a in value.keys():
            print(value)
    else:
        print('Питомец не найден')
def delete():
    a = input('Введите имя питомца, которого нужно удалить: ')
    for key, value in pets.items():
        if a in value.keys():
            del pets[key]
            break
        else:
            print('Питомец не найден')

while 'stop' != uslovie:
    uslovie = input('Введите команду(create, list, read, update, delete, all, stop): ')
    if uslovie == 'create':
        create()
    if uslovie == 'list':
        pets_list()
    if uslovie == 'update':
        update()
    if uslovie == 'read':
        read()
    if uslovie == 'delete':
        delete()
    if uslovie == 'all':
        print(pets)
#https://github.com/MishinIgor/Pract1.git
#PR9.2
