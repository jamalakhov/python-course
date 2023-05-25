# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

def get_count_desk(count_student_class, count_students_desk):
    return (count_student_class + count_students_desk - 1) // count_students_desk


class1 = int(input('Введите количество учащихся в классе 1: '))
class2 = int(input('Введите количество учащихся в классе 2: '))
class3 = int(input('Введите количество учащихся в классе 3: '))

count_desk = 0
count_students_desk = 2

count_desk += get_count_desk(class1, count_students_desk)
count_desk += get_count_desk(class2, count_students_desk)
count_desk += get_count_desk(class3, count_students_desk)

print(count_desk)