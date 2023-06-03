# 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа: n — кол-во элементов первого множества, m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def find_common_elements(n, m):
    set1 = set()
    set2 = set()

    print("Введите элементы множества 1:")
    for _ in range(n):
        element = int(input())
        set1.add(element)

    print("Введите элементы множества 2:")
    for _ in range(m):
        element = int(input())
        set2.add(element)

    common_elements = sorted(set1.intersection(set2))
    return common_elements


n = int(input("Введите количество элементов для множества 1: "))
m = int(input("Введите количество элементов для множества 2: "))

result = find_common_elements(n, m)
print(result)