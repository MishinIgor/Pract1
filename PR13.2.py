class MyTurtle(object):
    posx = 0
    posy = 0
    move = 1
    def __init__(self,x,y,s):
        self.posx = x
        self.posy = y
        self.move = s

    def go_up(self):
        self.posy += self.move

    def go_down(self):
        self.posy -= self.move

    def go_left(self):
        self.posx -= self.move

    def go_right(self):
        self.posx += self.move

    def evolve(self):
        self.move += 1

    def degrade(self):
        if self.move == 0:
            print('Нельзя уменьшить количество ниже 0')
        else:
            self.move -= 1

    def count_moves(self,x,y):
        onx = abs(self.posx-x)
        ony = abs(self.posy-y)
        moveall = onx + ony
        print(f'До точки ({x},{y}) нужно сделать {moveall} ходов')
turt = MyTurtle(3,6,2)

print(f'Моя черепаха находится в х: {turt.posx}, в у: {turt.posy}, и перемещается на {turt.move} клеток:')
turt.go_up()
turt.go_up()
print(f'Моя черепаха находится в х: {turt.posx}, в у: {turt.posy}, и перемещается на {turt.move} клеток:')
turt.count_moves(5,7)

#https://github.com/MishinIgor/Pract1.git
#PR13.2
