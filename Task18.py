# 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

def find_closest_element(arr, x):
    closest = None
    min_diff = float('inf')

    for num in arr:
        diff = abs(num - x)
        if diff < min_diff:
            closest = num
            min_diff = diff

    return closest

def create_arr(n) :
    list = []

    for i in range(n) :
        element = int(input('Введите элемент массива: '))
        list.insert(i, element)

    return list

N = int(input("Введите количество элементов в массиве: "))
arr = create_arr(N)
number = int(input("Введите число, чтобы найти ближайший элемент: "))

closest_element = find_closest_element(arr, number)
print(closest_element)