import random

def addmatr(): #Функция генерирования матрицы размера x,y
    x = int(input('Введите количество строк: '))
    y = int(input('Введите количество столбцов: '))
    k = [[random.randint(-200,200) for i in range(x)]for j in range(y)]
    return k

def pl(a):  #функция печати матрицы
    for i in a:
        print(*i)

def msum(a,b): #Функция вычисления суммы матриц
    result = [map(sum, zip(*i)) for i in zip(a, b)]
    return result

m1 = addmatr()
m2 = addmatr()
m3 = msum(m1,m2)

pl(m1)
print()
pl(m2)
print()
pl(m3)
#https://github.com/MishinIgor/Pract1.git
#PR10.1
