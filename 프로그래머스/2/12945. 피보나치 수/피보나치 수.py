def solution(n):
    pre, current = 0, 1

    for _ in range(2, n+1):
        current, pre = current + pre, current
    return current % 1234567