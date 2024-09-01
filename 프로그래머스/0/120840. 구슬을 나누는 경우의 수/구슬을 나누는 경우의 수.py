def factorial(num):
    answer = 1
    for i in range(1, num+1):
        answer *= i
    return answer

def solution(balls, share):
    n = factorial(balls)
    m = factorial(share)
    nm = factorial(balls - share)

    return n / (nm * m)