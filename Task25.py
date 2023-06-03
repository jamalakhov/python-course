# 25. Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

def track_character_occurrences(string):
    occurrences = {}
    result = []
    words = string.split()

    for word in words:
        if word not in occurrences:
            occurrences[word] = 0
        occurrences[word] += 1

        if occurrences[word] > 1:
            result.append(f"{word}_{occurrences[word] - 1}")
        else:
            result.append(word)

    return ' '.join(result)

input_string = input("Введите строку: ")
output_string = track_character_occurrences(input_string)

print(output_string)