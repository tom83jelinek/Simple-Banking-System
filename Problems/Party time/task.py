guest_list = []

while True:
    guest = input()
    if guest != '.':
        guest_list.append(guest)
    else:
        break

print(guest_list)
print(len(guest_list))
