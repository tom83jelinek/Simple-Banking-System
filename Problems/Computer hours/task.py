# Make sure your output matches the assignment *exactly*
hours_at_pc = int(input())

if hours_at_pc < 2:
    print('That seems reasonable')
elif 2 <= hours_at_pc < 4:
    print('Do you have time for anything else?')
else:
    print('You need to get outside more!')
