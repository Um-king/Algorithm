m = int(input())
n = int(input())
lst = []

for i in range(m, n+1):
    cnt = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)