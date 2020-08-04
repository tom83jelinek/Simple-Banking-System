n = int(input())
num_list = []

while n > 0:
    num_list.append(int(input()))
    n -= 1

print(sum(num_list) / len(num_list))