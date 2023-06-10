a = int(input("Введите число: "))
print('Вводите',a,'чисел через пробел: ')
k = [int(i) for i in input().split()]
n=0
p=[]
p.append(k[len(k)-1])
for i in range(0,len(k)-1):
    p.append(k[n])
    n+=1
print(p)
if a!=len(k):
    print('Программа конечно работает, но в следующий раз введите столько чисел сколько написано.')
#https://github.com/MishinIgor/Pract1.git
#PR6.2
