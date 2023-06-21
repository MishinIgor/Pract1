def rec(n):
    if len(n) == 0:
        return print('Конец списка')
    else:
        print(a[0], end=" ")
        del a[0]
        return rec(n)
a = [3,2,1,5,7,8,12,31]
rec(a)
#https://github.com/MishinIgor/Pract1.git
#PR11.1
