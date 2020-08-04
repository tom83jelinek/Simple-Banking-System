# put your python code here
while True:
    integer = int(input())

    if integer < 10:
        continue
    elif integer > 100:
        break
    else:
        print(integer)

else:
    print('Done reading.')
