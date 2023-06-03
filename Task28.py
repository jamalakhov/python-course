# 28. Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum_recursive(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_recursive(a - 1, b + 1)
    
num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))
result = sum_recursive(num_a, num_b)
print(result)