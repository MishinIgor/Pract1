num = {}
a = int(input('Введите левую границу интервала: '))
b = int(input('Введите правую границу интервала: '))
if a>b:
    for i in reversed(range(b, a+1)):
        num[i]= i**i
else:
    for i in range(a, b+1):
        num[i]= i**i
print(num)
#https://github.com/MishinIgor/Pract1.git
#PR8.2
