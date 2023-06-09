a = int(input('Введите левую границу интервала: '))
b = int(input('Введите правую границу интервала: '))
k = ''
for i in range(a,b):
    if i%2==0:
        k = k + ' ' + str(i)
print('Чётные числа в этом промежутке:'+k)
#https://github.com/MishinIgor/Pract1.git
#PR4.3
