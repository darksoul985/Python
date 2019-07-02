# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    vol = number * 10 ** ndigits
    if (vol % 1)+ 0.5 > 1:
        vol = int(vol + 1)/ 10 ** ndigits
    else:
        vol = int(vol) / 10 ** ndigits

    return vol

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    oper = list(str(ticket_number))
    if (len(oper))  is not 6:
        oper = ('В вашем билете слишком много/ слишком мало цифр')
        return oper
    else:
        sum_1 = int(oper[0]) + int(oper[1]) + int(oper[2])
        sum_2 = int(oper[3]) + int(oper[4]) + int(oper[5])
        if sum_1 == sum_2:
            oper = 'Ваш билет счастливый'
            return oper
        else:
            oper = 'Ваш билет счастливый'
            return oper

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))