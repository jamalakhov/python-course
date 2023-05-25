# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

def powers_of_two(N):
    powers = []
    power = 1

    while power <= N:
        powers.append(power)
        power *= 2

    return powers

N = int(input("Enter a number: "))

result = powers_of_two(N)
print("Powers of two not exceeding", N, ":")
for power in result:
    print(power)