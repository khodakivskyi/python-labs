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


task05()