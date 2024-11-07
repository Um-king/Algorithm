def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def solution(n, m):

    x = gcd(n, m)
    y = (n * m) // x

    return [x, y]
