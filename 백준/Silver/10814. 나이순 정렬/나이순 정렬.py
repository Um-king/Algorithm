n = int(input())
lst = []

for _ in range(n):
    x, y = input().split()

    lst.append([int(x), y])

for i,j in sorted(lst, key=lambda x:x[0]):
    print(i, j)