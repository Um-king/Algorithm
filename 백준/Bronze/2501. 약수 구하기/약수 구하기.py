n, k = map(int, input().split())
lst = []

for i in range(1, (n//2 + 1)):
    if n % i == 0:
        lst.append(i)

lst.append(n)

print(0 if len(lst) < k else lst[k-1])