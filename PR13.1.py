class Cassa(object):
    money = 1000

    def __init__(self, m):
        self.money = m

    def top_up(self):
        x = float(input('Внести: '))
        self.money += x

    def count_1000(self):
        print(f'В кассе {int(self.money // 1000)} тысяч')

    def top_up(self):
        x = float(input('Внести: '))
        self.money += x

    def take_away(self):
        x = float(input('Вывести: '))
        if x > self.money:
            print('Ошибка, таких денег в кассе нет.')
        else:
            self.money -= x

c1 = Cassa(50)
c1.top_up()
c1.count_1000()
c1.take_away()
print(c1.money)
c1.take_away()

#https://github.com/MishinIgor/Pract1.git
#PR13.1
