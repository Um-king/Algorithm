def gcd(x ,y):
    while y != 0:
        x, y = y, x%y
    return x

def solution(n, m):
    gcd_value = gcd(n, m)
    lcm_value = (n * m) // gcd_value
    return [gcd_value, lcm_value]