def can_afford(money, animals):
    while animals:
        item = animals.popitem()
        if item[1] <= money:
            affordable_animal = item
            break
        else:
            affordable_animal = ('None', -1)

    return affordable_animal[0].lower(), money // affordable_animal[1]


price_list = {'Chicken': 23, 'Goat': 678, 'Pig': 1296, 'Cow': 3848, 'Sheep': 6769}
users_balance = int(input())

animal, counts = can_afford(users_balance, price_list)

if counts > 1 and not animal == 'sheep':
    print(f'{counts} {animal}s')
elif counts == 1 or animal == 'sheep':
    print(f'{counts} {animal}')
else:
    print('None')
