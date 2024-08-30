def solution(a, b):
    answer = 0
    if a % 2 and b % 2:
        answer = a**2 + b**2
    elif not a % 2 and not b % 2:
        answer = abs(a - b)
    else:
        answer = 2 * (a + b)
    return answer