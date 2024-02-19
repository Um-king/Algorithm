def solution(n):
    return min(list(filter(lambda x: n % x == 1, range(1, n))))