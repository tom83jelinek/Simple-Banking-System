float_list = []

while True:
    float_ = input()
    if float_ != '.':
        float_list.append(float(float_))
    else:
        break

print(min(float_list))
