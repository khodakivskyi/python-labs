class Human:
    default_name = "Unknown"
    default_age = 0

    def __init__(self, name=None, age=None, money=0, house=None):
        if name is None:
            name = Human.default_name
        if age is None:
            age = Human.default_age
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Будинок: {self.__house}")
        print(f"Гроші: {self.__money}")

    @staticmethod
    def default_info():
        print(f"Ім'я за замовчуванням: {Human.default_name}")
        print(f"Вік за замовчуванням: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount=10):
        if self.__house is not None:
            print(f"Попередження: У вас вже є будинок!")
            return False
        final_price = house.final_price(discount)
        if self.__money < final_price:
            print(f"Попередження: Недостатньо грошей! У вас {self.__money}, а потрібно {final_price}")
            return False
        else:
            self.__make_deal(house, final_price)
            print(f"Будинок успішно куплено! Залишок грошей: {self.__money}")
            return True


class House:
    def __init__(self, area=100, price=100000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return round(self._price * (1 - discount / 100))


class SmallHouse(House):
    def __init__(self, price=100000):
        super().__init__(area=40, price=price)


if __name__ == "__main__":
    print("Довідкова інформація")
    Human.default_info()
    print()

    print("Створення об'єкта Human")
    human = Human("Іван", 25)
    human.info()
    print()

    print("Створення об'єкта SmallHouse")
    small_house = SmallHouse(price=50000)
    print(f"Площа SmallHouse: {small_house._area} м², ціна: {small_house._price}")
    print()

    print("Спроба купити будинок (має не вдатися)")
    human.buy_house(small_house)
    print()

    print("Збільшення грошей")
    human.earn_money(60000)
    human.info()
    print()

    print("Спроба купити будинок знову (має вдатися)")
    human.buy_house(small_house)
    print()

    print("Фінальний стан об'єкта Human")
    human.info()

