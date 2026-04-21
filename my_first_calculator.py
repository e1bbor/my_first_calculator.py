# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

import math

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply, divide, find square roots, and calculate exponentials for whole numbers from 0 to 50')
sign = input('What do you want to do? +, -, /, *, sqrt, or ^: ')

if sign == 'sqrt':
    num1 = int(input('Please choose your number: '))
    result = math.sqrt(num1)
    print(f"√{num1} = {result}")
else:
    num1 = int(input('Please choose your first number: '))
    num2 = int(input('Please choose your second number: '))

    if sign == '+':
        result = num1 + num2
        print(f"{num1}+{num2} = {result}")
    elif sign == '-':
        result = num1 - num2
        print(f"{num1}-{num2} = {result}")
    elif sign == '*':
        result = num1 * num2
        print(f"{num1}*{num2} = {result}")
    elif sign == '/':
        result = num1 / num2
        print(f"{num1}/{num2} = {result}")
    elif sign == '^':
        result = num1 ** num2
        print(f"{num1}^{num2} = {result}")

print("Thanks for using this calculator, goodbye :)")
