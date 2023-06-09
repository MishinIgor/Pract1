a = int(input('Введите пятизначное целое число: '))
if a<=9999:
    print('Вы ввели не корректное число!!!')
else:
    x = [int(k) for k in str(a)]
    f1 = (x[3]**x[4])*x[2]/(x[0]-x[1])
    print(f1)
#https://github.com/MishinIgor/Pract1.git
#PR2.2
