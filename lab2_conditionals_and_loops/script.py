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

    if price > 500:
        price -= price * 0.03
    elif price > 1000:
        price -= price * 0.05

    print("price:", price)


def task3(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0:
        print('Сторони мають бути числами, а також більшими за 0')
        return

    s = (2 * a + b) / 2
    if s % 2 == 0:
        print(s / 2)
    else:
        print("Не можу ділити на 2!")


def task4(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a < 0 or b < 0 or a > b:
        print("Передано невірні дані")
        return

    result_sum = 0
    for num in range(a, b):
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
    for num in range(a, b):
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


def task8(n):
    if not isinstance(n, int) or n <= 1:
        print("Передано не вірні дані")
        return

    k=0
    while pow(5,k)<=n:
        k+=1

    print(k)


def task9(n):
    if not isinstance(n, (int, float)):
        print("Передано не вірне значення")
        return

    for i in range(1, n+1):
        square=pow(i,2)
        if square > n:
            print("Перше число більше за n:", square)
            return

def task10(n):
    if not isinstance(n, (int, float)):
        print("Передано не вірне значення")
        return

    i=1
    while n < pow(i,2)+1:
        i+=1

    print("Перше число більше за n:", i+1)