s1 = [int(i) for i in input('Введите числа через пробел для s1: ').split()]
s2 = set(s1)
for i in s2:
    flag=0
    for j in s1:
        if j == i:
            flag+=1
            if flag == 2:
                print(i,'YES')
                break
    if flag == 1:
        print(i,'NO')
#https://github.com/MishinIgor/Pract1.git
#PR7.3
