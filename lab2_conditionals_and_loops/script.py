import random
import math

def task1():
    numbers = [random.randint(0, 100) for _ in range(10)]
    first_half = [n for n in numbers if n <= 50]
    print(numbers)
    print(first_half)


def task2(price):
    if not isinstance(price, (int, float)) or price < 0:
        print('Ціна має бути числом, а також більшою за 0')
        return

    if price > 1000:
        price -= price * 0.05
    elif price > 500:
        price -= price * 0.03

    print("price:", price)


def task3(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0:
        print('Сторони мають бути числами, а також більшими за 0')
        return

    if 2 * a <= b:
        print("Неможливо побудувати рівнобедрений трикутник з такими сторонами")
        return

    s = (b * math.sqrt(4 * a * a - b * b)) / 4
    if int(s) % 2 == 0:
        print(s / 2)
    else:
        print("Не можу ділити на 2!")


def task4(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > b:
        print("Передано невірні дані")
        return

    result_sum = 0
    for num in range(a, b + 1):
        if isinstance(num, int):
            result_sum += num

    print(result_sum)


def task5():
    while True:
        a_str = input("Введіть число A: ")
        b_str = input("Введіть число B (B > A): ")

        if a_str.replace('.', '', 1).isdigit() and b_str.replace('.', '', 1).isdigit():
            a = float(a_str)
            b = float(b_str)
            if a < b:
                break
            else:
                print("Число B має бути більше за A. Спробуйте ще раз.")
        else:
            print("Введіть правильні числа!")

    a = math.ceil(a)
    b = math.floor(b)
    result_sum = 0
    for num in range(a, b + 1):
        result_sum += pow(num, 2)

    print(result_sum)


def task6():
    while True:
        a_str = input("Введіть число A: ")
        b_str = input("Введіть число B (B >= A): ")

        if a_str.replace('.', '', 1).isdigit() and b_str.replace('.', '', 1).isdigit():
            a = float(a_str)
            b = float(b_str)
            if a < b:
                break
            else:
                print("Число B має бути більше за A. Спробуйте ще раз.")
        else:
            print("Введіть правильні числа!")

    a = math.ceil(a)
    b = math.floor(b)
    result_sum = 0
    while a <= b:
        result_sum += a
        a += 1

    print(result_sum)


def task7():
    while True:
        a_str = input("Введіть число A: ")

        if a_str.replace('.', '', 1).isdigit():
            a = float(a_str)
            a = math.ceil(a)
            if 50 >= a >= 0:
                break
            else:
                print("Введено невірну число.")
        else:
            print("Введено невірну число.")

    result_sum = 0
    for num in range(a, 50):
        result_sum += pow(num, 2)

    print(result_sum)


def task8(n):
    if not isinstance(n, int) or n <= 1:
        print("Передано не вірні дані")
        return

    k = 0
    while pow(5, k) <= n:
        k += 1

    print(k)


def task9(n):
    if not isinstance(n, (int, float)):
        print("Передано не вірне значення")
        return

    for i in range(1, int(n) + 2):
        square = pow(i, 2)
        if square > n:
            print("Перше число більше за n:", square)
            return


def task10(n):
    if not isinstance(n, (int, float)):
        print("Передано не вірне значення")
        return

    i = 1
    while pow(i, 2) + 1 <= n:
        i += 1

    if n <0:
        print("Перше число більше за n: 1")
    else:
        print("Перше число більше за n:", pow(i, 2) + 1)


def task11(d, m):
    if not isinstance(d, int) or not isinstance(m, int) or d <= 0 or m <= 0:
        return "Передано не вірні значення"

    days_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if m not in days_in_month or d < 1 or d > days_in_month[m]:
        return "Невірна дата"

    match m:
        case 1:
            return "Козеріг" if d <= 19 else "Водолій"
        case 2:
            return "Водолій" if d <= 18 else "Риби"
        case 3:
            return "Риби" if d <= 20 else "Овен"
        case 4:
            return "Овен" if d <= 19 else "Телець"
        case 5:
            return "Телець" if d <= 20 else "Близнюки"
        case 6:
            return "Близнюки" if d <= 21 else "Рак"
        case 7:
            return "Рак" if d <= 22 else "Лев"
        case 8:
            return "Лев" if d <= 22 else "Діва"
        case 9:
            return "Діва" if d <= 22 else "Терези"
        case 10:
            return "Терези" if d <= 22 else "Скорпіон"
        case 11:
            return "Скорпіон" if d <= 22 else "Стрілець"
        case 12:
            return "Стрілець" if d <= 21 else "Козеріг"
        case _:
            return "Невірна дата"


def task12(n: int, w: float):
    if not isinstance(n, int) or not isinstance(w, float) or n <= 0 or n > 5 or w <= 0:
        print("Передано не вірні значення")
        return

    match n:
        case 1:
            print("Маса тіла в кг:", w)
            return
        case 2:
            print("Маса тіла в кг:", w / 1000000)
            return
        case 3:
            print("Маса тіла в кг:", w / 1000)
            return
        case 4:
            print("Маса тіла в кг:", w * 1000)
            return
        case 5:
            print("Маса тіла в кг:", w * 100)
            return
        case _:
            return


print("\n1. TASK1 - Генерація випадкових чисел:")
task1()

# Task 2 - Розрахунок знижки
print("\n2. TASK2 - Розрахунок знижки:")
print("Тест 1 (звичайна ціна 300 грн):")
task2(300)
print("Тест 2 (знижка 3% - 600 грн):")
task2(600)
print("Тест 3 (знижка 5% - 1200 грн):")
task2(1200)
print("Тест 4 (негативна ціна):")
task2(-100)
print("Тест 5 (неправильний тип):")
task2("abc")

# Task 3 - Розрахунок площі
print("\n3. TASK3 - Розрахунок площі рівнобедреного трикутника:")
print("Тест 1 (a=5, b=8 - парна площа):")
task3(5, 8)
print("Тест 2 (a=3, b=7 - непарна площа):")
task3(3, 7)
print("Тест 3 (негативні значення):")
task3(-2, 5)
print("Тест 4 (неправильний тип):")
task3("a", 5)

# Task 4 - Сума цілих чисел в діапазоні
print("\n4. TASK4 - Сума цілих чисел від A до B:")
print("Тест 1 (A=1, B=5):")
task4(1, 5)
print("Тест 2 (A=3, B=8):")
task4(3, 8)
print("Тест 3 (A > B):")
task4(5, 3)
print("Тест 4 (негативні значення):")
task4(-1, 5)

# Task 5 - Сума квадратів (з вводом)
print("\n5. TASK5 - Сума квадратів (з вводом):")
print("Для тестування введіть: A=2.3, B=5.7")
print("Очікуваний результат: 3² + 4² + 5² = 9 + 16 + 25 = 50")
task5()

# Task 6 - Сума чисел в діапазоні (з вводом)
print("\n6. TASK6 - Сума чисел в діапазоні (з вводом):")
print("Для тестування введіть: A=1.5, B=4.2")
print("Очікуваний результат: 2 + 3 + 4 = 9")
task6()

# Task 7 - Сума квадратів до 50 (з вводом)
print("\n7. TASK7 - Сума квадратів до 50 (з вводом):")
print("Для тестування введіть: A=3.7")
print("Очікуваний результат: 4² + 5² + ... + 49²")
task7()

# Task 8 - Знаходження степеня 5
print("\n8. TASK8 - Знаходження степеня 5:")
print("Тест 1 (n=25, очікуємо k=3, бо 5³=125 > 25):")
task8(25)
print("Тест 2 (n=125, очікуємо k=4, бо 5⁴=625 > 125):")
task8(125)
print("Тест 3 (n=1, помилка):")
task8(1)
print("Тест 4 (неправильний тип):")
task8("abc")

# Task 9 - Перший квадрат більший за n
print("\n9. TASK9 - Перший квадрат більший за n:")
print("Тест 1 (n=10, очікуємо 16=4²):")
task9(10)
print("Тест 2 (n=25, очікуємо 36=6²):")
task9(25)
print("Тест 3 (n=0, очікуємо 1=1²):")
task9(0)
print("Тест 4 (неправильний тип):")
task9("abc")

# Task 10 - Перше число за умовою
print("\n10. TASK10 - Перше число за умовою:")
print("Тест 1 (n=10, очікуємо 4, бо 3²+1=10, наступне 4²+1=17):")
task10(10)
print("Тест 2 (n=5, очікуємо 3, бо 2²+1=5, наступне 3²+1=10):")
task10(5)
print("Тест 3 (неправильний тип):")
task10("abc")

# Task 11 - Знак зодіаку
print("\n11. TASK11 - Знак зодіаку:")
print("Тест 1 (15 січня):", task11(15, 1))
print("Тест 2 (20 січня):", task11(20, 1))
print("Тест 3 (10 лютого):", task11(10, 2))
print("Тест 4 (25 лютого):", task11(25, 2))
print("Тест 5 (15 березня):", task11(15, 3))
print("Тест 6 (25 березня):", task11(25, 3))
print("Тест 7 (невірна дата 32 січня):", task11(32, 1))
print("Тест 8 (невірний місяць 15):", task11(15, 13))

# Task 12 - Конвертація маси
print("\n12. TASK12 - Конвертація маси:")
print("Тест 1 (кілограми, w=1000):")
task12(1, 1000.0)
print("Тест 2 (міліграми, w=1000000):")
task12(2, 1000000.0)
print("Тест 3 (грами, w=5000):")
task12(3, 5000.0)
print("Тест 4 (тони, w=2.5):")
task12(4, 2.5)
print("Тест 5 (центи, w=10):")
task12(5, 10.0)
print("Тест 6 (n=0, помилка):")
task12(0, 100.0)
print("Тест 7 (n=6, помилка):")
task12(6, 100.0)
print("Тест 8 (w=-100, помилка):")
task12(1, -100.0)