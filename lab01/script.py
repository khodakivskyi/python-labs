# 1
a = float(input())
b = float(input())
c = float(input())
d = float(input())

# 2
res_list = [a + b, c - d, a * d, b / c, pow(a, c), a // c, d % b]

# 3
print(res_list)
print("Кількість елементів:", len(res_list))

print("Парні елементи списку: ")
for value in res_list:
    if value % 2 == 0:
        print(value)

# 4
temp=res_list[2]
res_list[2]=res_list[5]
res_list[5]=temp
print("2 і 5 елемент масиву змінено:", res_list)

# 5
name=input()
print("Виконавець лабораторної роботи:", name)

print("Висновки:")
print("Ознайомився з алгоритмами послідовної (лінійної) структури.")
print("З процедурами запуску програм, які реалізують ці алгоритми на мові Python.")
print("Ознайомився з інтегрованим середовищем розробки integrated development environment (IDLE).")
