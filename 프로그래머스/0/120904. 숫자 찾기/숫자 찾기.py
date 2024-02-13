def solution(num, k):
    n = str(num).find(str(k))
    return n if n == -1 else n + 1