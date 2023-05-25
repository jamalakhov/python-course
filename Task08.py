# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('Введите ширину шоколадки: '))
height = int(input('Введите высоту шоколадки: '))
count_slice = int(input('Введите количество долек: '))

if count_slice <= width * height and (count_slice % width == 0 or count_slice % height == 0):
    print("yes")
else:
    print("no")