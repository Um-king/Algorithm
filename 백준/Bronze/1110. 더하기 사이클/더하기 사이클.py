n = input()
n = "0" + n if len(n) == 1 else n
n2 = n
cnt = 1

while True:
    s = str(int(n2[0]) + int(n2[-1]))
    s = "0" + s if len(s) == 1 else s
    m = n2[-1] + s[1]

    if m == n:
        break

    n2 = m
    cnt += 1

print(cnt)