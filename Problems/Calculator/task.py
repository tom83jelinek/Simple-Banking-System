# put your python code here
first_number = float(input())
second_number = float(input())
math_operation = input()

non_zero_operations = ('mod', 'div', '/')

if second_number == 0 and math_operation in non_zero_operations:
    print('Division by 0!')
elif math_operation.lower() == 'mod':
    print(first_number % second_number)
elif math_operation.lower() == 'pow':
    print(first_number ** second_number)
elif math_operation.lower() == 'div':
    print(first_number // second_number)
elif math_operation == '+':
    print(first_number + second_number)
elif math_operation == '-':
    print(first_number - second_number)
elif math_operation == '*':
    print(first_number * second_number)
elif math_operation == '/':
    print(first_number / second_number)
else:
    print('Unknown operation!')
