# my_first_calculator.py by AceLewis
# TODO: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to 50')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
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

print("Thanks for using this calculator, goodbye :)")
