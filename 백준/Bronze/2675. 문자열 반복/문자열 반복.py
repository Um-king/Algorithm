n = int(input())

for i in range(n):
    x, y = input().split()
    print(''.join([j * int(x) for j in y]))