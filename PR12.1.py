class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

autobus = Transport('Renault Logan', 180, 12)
print(f'Марка автомобиля: {autobus.name},Скорость: {autobus.max_speed},Пробег: {autobus.mileage}')
#https://github.com/MishinIgor/Pract1.git
#PR12.1
