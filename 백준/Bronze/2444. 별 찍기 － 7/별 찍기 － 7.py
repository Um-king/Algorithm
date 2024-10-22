n = int(input())

for i in range(n):
    print(" " * (n - 1 - i), end = '')
    print("*" * (i + (1 + i)))

n -= 1
for i in range(n):
    print(" " * (i + 1), end = '')
    print("*" * ((n - i) * 2 - 1))
