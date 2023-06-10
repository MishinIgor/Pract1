norma = int(input("Введите норму веса для лодки: "))
ribak = int(input("Введите количество рыбаков: "))
x = []
n = 0
lodok = 0
for i in range(0,ribak):
    print("Введите вес",i+1,"рыбака: ", end=" ")
    x.append(int(input()))
p = sorted(x)
while ribak>0:
    lodok+=1
    if p[ribak-1]+p[n]>norma:
        ribak-=1
    else:
        ribak-=2
        n+=1
print("Необходимо",lodok," для транспортировки")
#https://github.com/MishinIgor/Pract1.git
#PR6.3
