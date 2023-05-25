# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6 

number = int(input('Введите натуральное число: '))
position = -1
count = 2

f1 = 0
f2 = 1

for i in range(number + 1) :
    current_f = f1 + f2
    count += 1
    
    if number == current_f :
        position = count
        break

    f1 = f2
    f2 = current_f

print(position)