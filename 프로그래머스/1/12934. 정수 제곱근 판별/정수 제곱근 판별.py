import math

def solution(n):
    # return (math.isqrt(n) + 1) ** 2 if math.isqrt(n) ** 2 == n else -1
     return ((n ** .5) + 1) ** 2 if n ** .5 % 1 == 0 else -1