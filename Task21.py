# 21. Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

dictionary_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]

def print_unique_values(dictionary_list):
    unique_values = set()

    for dictionary in dictionary_list:
        for value in dictionary.values():
            unique_values.add(value.strip())

    print(unique_values)

print_unique_values(dictionary_list)