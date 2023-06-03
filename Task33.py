# 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def replace_grades(num_grades, grades):
    min_grade = min(grades)
    max_grade = max(grades)

    new_grades = []

    for grade in grades :
        if grade == max_grade :
            new_grades.append(min_grade)
        else :
            new_grades.append(grade)

    return new_grades

num_grades = int(input("Введите количество оценок: "))
grades = list(map(int, input("Введите оценки через пробел: ").split()))

new_grades = replace_grades(num_grades, grades)
print(' '.join(map(str, new_grades)))