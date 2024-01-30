def solution(n):
    return len(list(filter(lambda x : n % (x + 1) == 0, range(n))))