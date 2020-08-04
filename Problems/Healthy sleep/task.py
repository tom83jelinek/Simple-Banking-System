a, b, h = int(input()), int(input()), int(input())

if h < a:
    print('Deficiency')
elif h > b:
    print('Excess')
elif a <= h <= b:
    print('Normal')
