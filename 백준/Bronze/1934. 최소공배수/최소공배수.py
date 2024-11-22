def gcd(x, y):

    while y > 0:
        x, y = y, x % y

    return x

n= int(input())

for _ in range(n):
    x, y = map(int, input().split())
    num = gcd(x, y)
    print((x*y)//num)