# 최소공배수
def solution(n):
    return min([i for i in range(n, (n * 6) + 1) if i % n == 0 and i % 6 == 0]) // 6