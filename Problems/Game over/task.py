scores = input().split()
# put your python code here
lives = 3
score = 0

while lives > 0 and scores:
    answer = scores.pop(0)

    if answer == 'C':
        score += 1
    elif answer == 'I':
        lives -= 1

if lives > 0:
    print(f'You won\n{score}')
else:
    print(f'Game over\n{score}')
