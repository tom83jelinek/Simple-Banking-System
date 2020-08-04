army_of_units = int(input())

if army_of_units < 1:
    print('no army')
elif 1 <= army_of_units <= 9:
    print('few')
elif 10 <= army_of_units <= 49:
    print('pack')
elif 50 <= army_of_units <= 499:
    print('horde')
elif 500 <= army_of_units <= 999:
    print('swarm')
else:
    print('legion')
