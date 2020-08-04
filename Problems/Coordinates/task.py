def cartesian_quadrant(x_axis, y_axis):
    if x_axis > 0.0 and y_axis > 0.0:
        return 'I'
    elif x_axis < 0.0 < y_axis:
        return 'II'
    elif x_axis < 0.0 and y_axis < 0.0:
        return 'III'
    else:
        return 'IV'


x, y = float(input()), float(input())

print(cartesian_quadrant(x, y))
