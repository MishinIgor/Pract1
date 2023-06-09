a = float(input('Введите минимальную сумму инвестиций: '))
mike = float(input('У Майка денег: '))
ivan = float(input('У Ивана денег: '))

if mike>a and ivan>a:
    print(2)
elif mike>a and ivan<a:
    print('Mike')
elif mike<a and ivan>a:
    print('Ivan')
elif mike+ivan>a:
    print(1)
elif mike+ivan<a:
    print(0)
#https://github.com/MishinIgor/Pract1.git
#PR3.3
