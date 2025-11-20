class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        self.__speed = max(0, self.__speed - 5)
        return self.__speed

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


def task03():
    car = Car("Toyota", "Corolla", 2020)
    print(f"Тестуємо автомобіль {car}")
    for _ in range(5):
        car.accelerate()
        print(f"Поточна швидкість: {car.get_speed()} км/год")
    for _ in range(5):
        car.brake()
        print(f"Поточна швидкість: {car.get_speed()} км/год")


task03()

