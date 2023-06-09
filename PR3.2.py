slovo = input('Введите слово  из маленьких латинских букв: ')
x = [str(i) for i in str(slovo)]
sogl=0; glas=0; glass=['a','e','i','o','u']; list=[0,0,0,0,0];
for t in x:
    flag=-1
    for k in glass:
        flag+=1
        if t==k:
            glas+=1
            list[flag]+=1
sogl = len(x)-glas
print("Гласных:",glas, "Согласных:",sogl)
flag=-1
for i in list:
    flag+=1
    if i > 0:
        print(glass[flag],list[flag],sep=" - ")
    else:
        print(glass[flag],i>0,sep=" - ")
#https://github.com/MishinIgor/Pract1.git
#PR3.2

