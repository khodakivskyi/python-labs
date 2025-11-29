class Apple:
    states = ["Відсутнє", "Цвітіння", "Зелене", "Червоне"]

    def __init__(self, index):
        self._index = index
        self._state = Apple.states[0]

    def grow(self):
        current_index = Apple.states.index(self._state)
        if current_index < len(Apple.states) - 1:
            self._state = Apple.states[current_index + 1]

    def is_ripe(self):
        return self._state == Apple.states[-1]

    def get_state(self):
        return self._state

    def get_index(self):
        return self._index


class AppleTree:
    def __init__(self, apple_count):
        self.apples = [Apple(i + 1) for i in range(apple_count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print("Урожай зібрано!")
            self._tree.give_away_all()
        else:
            print("Попередження: яблука ще не дозріли!")

    @staticmethod
    def apple_base(apples):
        print("Довідка по яблукам:")
        print(f"Кількість яблук: {len(apples)}")
        for apple in apples:
            print(f"Яблуко №{apple.get_index()}: {apple.get_state()}")


def task03():
    apple1 = Apple(1)
    apple2 = Apple(2)
    apple3 = Apple(3)
    
    apples_list = [apple1, apple2, apple3]
    Gardener.apple_base(apples_list)
    print()

    tree = AppleTree(5)
    gardener = Gardener("Іван", tree)
    
    print("Робота садівника над деревом...")
    gardener.work()  
    gardener.work() 
    print()

    print("Спроба зібрати урожай:")
    gardener.harvest()
    print()

    print("Продовження догляду за деревом...")
    gardener.work()  
    print()

    print("Спроба зібрати урожай знову:")
    gardener.harvest()
    print()

    print("Стан дерева після збору урожаю:")
    print(f"Кількість яблук на дереві: {len(tree.apples)}")


task03()