# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Input: 5
# Output: 120

number = int(input('Введите число: '))

sum = 1
temp = 1

for i in range(number) :
    sum *= temp
    temp += 1

print(sum)