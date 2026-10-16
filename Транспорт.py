
class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f'Транспорт - {self.name}'


class Car(Transport):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def description(self):
        return f'Транспорт - {self.name} Мощность - {self.power}'


class Plane(Transport):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def description(self):
        return f'Транспорт - {self.name}, Размах крыльев - {self.size}'


class Bike(Transport):
    def __init__(self, name, tank):
            super().__init__(name)
            self.tank = tank



    def description(self):
        return f'Транспорт - {self.name}, объем бака - {self.tank}'

#Данные выдуманы и не соответствуют реальности, гуглить времени не было
bike = Bike("Харлей", '100 куб.м.')
car = Car('Model S', '300 лс')
plane = Plane('Боинг 747', '65 м')

print(bike.description())
print(car.description())
print(plane.description())
