def solution(n):
    return sum(filter(lambda x:x%2 > 0, range(n + 1))) if n % 2 != 0 else sum(map(lambda x : x * x, filter(lambda x:x%2 == 0, range(n + 1))))