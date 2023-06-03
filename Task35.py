# 35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


# Пример использования:
num = int(input("Введите число: "))

if is_prime(num):
    print("yes")
else:
    print("no")
