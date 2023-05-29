# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

def shift_sequence(sequence, k):
    n = len(sequence)
    k = k % n

    if k == 0 :
        return sequence

    shifted_sequence = sequence[-k:] + sequence[:-k]

    return shifted_sequence

    # OR
    # for _ in range(k):
    #     sequence.insert(0, sequence.pop())
    
    # return sequence    

sequence = [1, 2, 3, 4, 5]
k = int(input("Введите шаг сдвига: "))

result = shift_sequence(sequence, k)
print(result)