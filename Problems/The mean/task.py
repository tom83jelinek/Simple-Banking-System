int_list = []

while True:
    integer = input()
    if integer != '.':
        int_list.append(int(integer))
    else:
        break

print(sum(int_list) / len(int_list))
