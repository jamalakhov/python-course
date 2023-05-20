# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

class1 = int(input('Введите количество учащихся в классе 1: '))
class2 = int(input('Введите количество учащихся в классе 2: '))
class3 = int(input('Введите количество учащихся в классе 3: '))

count_desk = 0
count_students = 2

count_desk += (class1 + count_students - 1) // count_students
count_desk += (class2 + count_students - 1) // count_students
count_desk += (class3 + count_students - 1) // count_students

print(count_desk)