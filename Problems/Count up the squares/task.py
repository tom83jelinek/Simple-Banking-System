# put your python code here
numbers = []
numbers_squared = []

while True:
    number = int(input())
    numbers.append(number)
    numbers_squared.append(number ** 2)

    if sum(numbers) == 0 and len(numbers) == 1:
        print(0)
        break
    elif sum(numbers) == 0 and len(numbers) > 1:
        print(sum(numbers_squared))
        break
