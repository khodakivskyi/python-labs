import random


def task01():
    while True:
        numbers_input = input("Введіть цілі числа через пробіл: ").split()
        numbers = []

        all_valid = True

        for x in numbers_input:
            try:
                numbers.append(int(x))
            except ValueError:
                print(f"Помилка: '{x}' — не ціле число.")
                all_valid = False

        if all_valid and numbers:
            break
        else:
            print("Спробуйте ще раз.\n")

    largest = max(numbers)
    print("Найбільший елемент:", largest)


def task02():
    while True:
        numbers_input = input("Введіть цілі числа через пробіл: ").split()
        numbers = []

        all_valid = True

        for x in numbers_input:
            try:
                numbers.append(int(x))
            except ValueError:
                print(f"Помилка: '{x}' — не ціле число.")
                all_valid = False

        if all_valid and numbers:
            break
        else:
            print("Спробуйте ще раз.\n")

    positive_numbers = [n for n in numbers if n > 0]
    others = [n for n in numbers if n <= 0]

    print("Вихідний список:", numbers)
    print("Додатні числа:", positive_numbers)
    print("Інші числа:", others)


def task03(numbers):
    if len(numbers) != 20:
        print("Помилка: список має містити рівно 20 елементів.")
        return

    odd_index_sum = 0
    for i in range(1, len(numbers), 2):
        try:
            odd_index_sum += float(numbers[i])
        except (ValueError, TypeError):
            pass

    print("Сума чисел з непарними індексами:", odd_index_sum)


def task04():
    numbers = [random.randint(-100, 100) for _ in range(30)]
    print("Вихідний список:", numbers)

    max_value = max(numbers)
    max_index = numbers.index(max_value)
    print(f"Максимальний елемент: {max_value}, індекс: {max_index}")

    odd_numbers = [n for n in numbers if n % 2 != 0]

    if odd_numbers:
        odd_numbers.sort(reverse=True)
        print("Непарні числа у порядку зменшення:", odd_numbers)
    else:
        print("Непарних чисел немає.")


def task05():
    numbers = [random.randint(-100, 100) for _ in range(30)]
    print("Вихідний список:", numbers)

    pairs = []
    for i in range(len(numbers)-1):
        if numbers[i] < 0 and numbers[i+1]<0:
            pairs.append((numbers[i], numbers[i+1]))

    print("Пари від’ємних чисел, що стоять поруч:", pairs)


def task06(numbers):
    if len(numbers) != 10:
        print("Помилка: список має містити рівно 10 елементів.")
        return

    if not all(isinstance(n, int) for n in numbers):
        print("Є елементи, які не є цілими числами")
        return

    max_value = max(numbers)

    numbers2 = []
    for num in numbers:
        if num != max_value:
            numbers2.append(pow(num, 2))

    numbers2.sort(reverse=True)

    print("Вихідний список:", numbers)
    print("Максимальний елемент:", max_value)
    print("Квадрати менших чисел у порядку зменшення:", numbers2)


def task07():
    numbers = []
    for _ in range(30):
        if random.choice([True, False]):
            numbers.append(random.randint(-100, 100))
        else:
            numbers.append(random.uniform(-100, 100))
    print("Вихідний список:", numbers)

    min_abs_value = min(numbers, key=abs)
    print("Мінімальний по модулю елемент:", min_abs_value)

    sorted_numbers = sorted(numbers)
    print("Список у порядку зростання:", sorted_numbers)


def task08():
    numbers = []
    for _ in range(30):
        if random.choice([True, False]):
            numbers.append(random.randint(-100, 100))
        else:
            numbers.append(random.uniform(-100, 100))
    print("Вихідний список:", numbers)

    numbers2 = []
    for i in range(0, len(numbers), 3):
        numbers2.append(numbers[i:i + 3])

    sorted_numbers2 = sorted(numbers2, key=lambda sublist: sum(map(abs, sublist)))

    print("Підсписки у порядку зростання за сумою абсолютних значень:")
    for obj in sorted_numbers2:
        print(obj)


task08()