def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x 

def solution(n, m):
    gcd_value = gcd(n, m) # 최대공약수
    lcm_value = (n * m) // gcd_value # 최소공배수
    return [gcd_value, lcm_value]
