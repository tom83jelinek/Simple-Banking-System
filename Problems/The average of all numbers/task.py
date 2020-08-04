# put your python code here
a, b = int(input()), int(input())
to_average = []

for number in range(a, b + 1):
    if number % 3 == 0:
        to_average.append(number)
    else:
        continue

print(sum(to_average) / len(to_average))
