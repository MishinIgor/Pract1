def fact(a):
    k=1
    for i in range(1,a+1):
        k*=i
    return(k)
x = []
t = int(input('Введите число: '))
for i in reversed(range(1,fact(t)+1)):
    x.append(fact(i))
print(x)
#https://github.com/MishinIgor/Pract1.git
#PR9.1
