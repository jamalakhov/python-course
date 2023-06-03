# 26. Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def power_recursive(a, b) :
    if b == 0 :
        return 1
    elif b < 0 :
        return 1 / power_recursive(a, -b)
    else :
        return a * power_recursive(a, b - 1)
    
num_a = int(input("Введите число A: "))
num_b = int(input("Введите степень B: "))
result = power_recursive(num_a, num_b)
print(result)