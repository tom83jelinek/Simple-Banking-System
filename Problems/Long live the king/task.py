def king_moves(column, row):
    if column in (1, 8) and row in (1, 8):
        return 3
    elif column in range(2, 8) and row in range(2, 8):
        return 8
    elif (column in (1, 8) or row in (1, 8)) \
            and (column in range(2, 8) or row in range(2, 8)):
        return 5
    else:
        return 'I do not know'


print(king_moves(int(input()), int(input())))
