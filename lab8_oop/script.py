import random


class Bank:
    def __init__(self, balance):
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Початковий баланс має бути додатнім числом")
        self.__balance = float(balance)

    @staticmethod
    def __validate_amount(amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сума операції має бути додатнім числом")
        return float(amount)

    def deposit(self, amount):
        amount = self.__validate_amount(amount)
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        amount = self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return round(self.__balance, 2)


class Coin:
    SIDES = ("heads", "tails")

    def __init__(self, side="heads"):
        if side not in self.SIDES:
            raise ValueError("Можливі значення: heads або tails")
        self.__sideup = side

    def toss(self):
        self.__sideup = random.choice(self.SIDES)
        return self.__sideup

    def get_sideup(self):
        return self.__sideup


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


class Dog:
    mammal = "ссавець"
    nature = "дружній"
    breed = "невідома порода"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name}, {self.age} роки, {self.breed}"

    def speak(self):
        return f"{self.name} каже: Гав!"

    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "mammal": self.mammal,
            "nature": self.nature,
            "breed": self.breed,
        }


class Beagle(Dog):
    nature = "цікавий та товариський"
    breed = "бігль"

    def track(self):
        return f"{self.name} відстежує запах."


class GermanShepherd(Dog):
    nature = "відданий та уважний"
    breed = "німецька вівчарка"

    def guard(self):
        return f"{self.name} охороняє територію."


class Husky(Dog):
    nature = "активний і товариський"
    breed = "хаскі"

    def pull_sled(self):
        return f"{self.name} тягне уявні сани."


class Pets:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_pet(self, pet):
        self.animals.append(pet)

    def show_pets(self):
        lines = [f"Домашні тварини власника {self.name}:"]
        for index, pet in enumerate(self.animals, start=1):
            info = pet.info()
            lines.append(
                f"{index}. {info['name']} ({info['breed']}), {info['age']} років, характер: {info['nature']}"
            )
        return "\n".join(lines)


def task01():
    bank_account = Bank(1500)
    bank_account.deposit(350.75)
    try:
        bank_account.withdraw(2000)
    except ValueError as error:
        print(f"{error}")
    bank_account.withdraw(250)
    print(f"Поточний баланс: {bank_account.get_balance()} грн")


def task02(tosses=10):
    coin = Coin()
    results = [coin.toss() for _ in range(tosses)]
    print(f"{tosses} підкидань: {', '.join(results)}")


def task03():
    car = Car("Toyota", "Corolla", 2020)
    print(f"Тестуємо автомобіль {car}")
    for _ in range(5):
        car.accelerate()
        print(f"Поточна швидкість: {car.get_speed()} км/год")
    for _ in range(5):
        car.brake()
        print(f"Поточна швидкість: {car.get_speed()} км/год")


def task04():
    pets = Pets("Андрій")
    dogs = [
        Beagle("Лаки", 3),
        GermanShepherd("Бруно", 5),
        Husky("Сніжок", 2),
    ]
    for dog in dogs:
        pets.add_pet(dog)
        print(f"{dog.describe()}")
        print(f"{dog.speak()}")
    print(pets.show_pets())
