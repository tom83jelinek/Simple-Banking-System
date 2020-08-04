biggest_cat_count = 0
cafe = ''

while True:
    cafe_cats = input().split()
    if cafe_cats[0] != 'MEOW':
        if int(cafe_cats[1]) > biggest_cat_count:
            biggest_cat_count = int(cafe_cats[1])
            cafe = cafe_cats[0]
        else:
            continue
    else:
        break

print(cafe)
