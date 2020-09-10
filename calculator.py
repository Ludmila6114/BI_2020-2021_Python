# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

x = int(input())
sign = input()
y = int(input())
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
                print('Please, check your input data. You do something wrong.')
