# 16. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

def count_occurrences(arr, x):
    count = 0

    for num in arr :
        if num == x :
            count += 1

    return count

def create_arr(n) :
    list = []

    for i in range(n) :
        element = int(input('Введите элемент массива: '))
        list.insert(i, element)

    return list

N = int(input("Введите количество элементов в массиве: "))
arr = create_arr(N)
number = int(input("Введите число для поиска: "))

occurrences = count_occurrences(arr, number)
print(occurrences)