# 23. Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

def count_elements_greater_than_previous(arr):
    count = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1

    return count

arr = [0, -1, 5, 2, 3]
count = count_elements_greater_than_previous(arr)
print(count)