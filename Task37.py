# 37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def print_reverse_sequence():
    num = int(input("Введите количество элементов: "))
    sequence = []

    for _ in range(num):
        element = int(input("Введите элемент: "))
        sequence.append(element)
    
    for i in range(num - 1, -1, -1):
        print(sequence[i], end=" ")

print_reverse_sequence()