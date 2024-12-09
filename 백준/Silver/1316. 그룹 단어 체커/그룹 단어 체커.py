n = int(input())
s = set()
cnt = n

for _ in range(n):
    s.add(input())

for i in s:
    for j in range(0, len(i) - 1):
        if i[j] == i[j+1]:
            pass
        elif i[j] in i[j+1:]:
            cnt -= 1
            break

print(cnt)