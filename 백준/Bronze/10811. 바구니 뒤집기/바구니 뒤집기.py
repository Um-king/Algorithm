n, m = map(int, input().split())

lst = [i + 1 for i in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    lst = lst[:x - 1] + lst[x - 1: y][::-1] + lst[y:]

for i in lst:
    print(i, end= ' ')