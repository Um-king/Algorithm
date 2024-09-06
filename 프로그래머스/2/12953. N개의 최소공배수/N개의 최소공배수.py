def gcd(x, y):
    a = min(x, y)
    b = max(x, y)

    if a == 0:
        return b
    else:
        return gcd(a, b%a)

def lcm(x, y):
    return (x*y)//gcd(x, y)

def solution(arr):
    answer = arr[0]

    for i in arr[1:]:
        answer = lcm(answer, i)

    return answer