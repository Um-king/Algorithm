a = int(input())
b = input()

total = 0

for i, j in enumerate(b[::-1]):
    print(int(a) * int(j))
    if i == 0:
        total += int(a) * int(j)
    else:
        total += int(a) * int(j) * (10 ** i)
print(total)
