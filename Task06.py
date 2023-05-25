# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:
# 385916 -> yes
# 123456 -> no

def get_sum(digit):
    sum = 0
    while digit > 0:
        sum += digit % 10
        digit //= 10
    return sum

ticket_number = input('Введите номер билета: ')
str_len = len(ticket_number)

if str_len % 2 != 0:
    print('Нам не получится сделать рассчеты, поскольку номер билета не четный')
else:
    head = int(ticket_number[0 : str_len // 2])
    foot = int(ticket_number[str_len // 2 : str_len])

    first_sum = get_sum(head)
    last_sum = get_sum(foot)
    
    if first_sum == last_sum:
        print('yes')
    else:
        print('no')