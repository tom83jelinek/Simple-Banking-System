student_score = int(input())
max_score = int(input())

percentage = 100 / max_score * student_score

if 100.0 >= percentage >= 90.0:
    print('A')
elif 90.0 > percentage >= 80.0:
    print('B')
elif 80.0 > percentage >= 70.0:
    print('C')
elif 70.0 > percentage >= 60.0:
    print('D')
else:
    print('F')