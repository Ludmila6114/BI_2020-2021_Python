# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print('Введите первое число:')
x = float(input())
print('Введите один из знаков: +, -, * или /')
sign = input()
print('Введите второе число:')
y = float(input())
if sign == '+':
    print(x + y)
else:
    if sign == '-':
        print(x - y)
    else:
        if sign == '*':
            print(x*y)
        else:
            if sign == '/' and y != 0:
                print(x/y)
            else:
                print('Проверьте свои данные, что-то не так.')
