class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

autobus = Transport('Renault Logan', 180, 12)
print(autobus.seating_capacity(50))
#https://github.com/MishinIgor/Pract1.git
#PR12.2
