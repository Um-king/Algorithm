n, m = map(int, input().split())
lst = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    for l in range(i, j + 1):
        lst[l-1] = k

for i in lst:
    print(i, end=' ')