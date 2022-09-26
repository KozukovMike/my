# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
first_number, operation, second_number = float(input()), input(), float(input())
if operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/':
    print(first_number / second_number)
elif operation == '%':
    print(first_number % second_number)
elif operation == '//':
    print(first_number // second_number)
else:
    print('к сожалению вы ввели неизвестную опирацию')
