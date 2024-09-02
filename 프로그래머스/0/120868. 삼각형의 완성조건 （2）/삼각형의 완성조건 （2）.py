def solution(sides):
    n, m = sorted(sides)
    answer = 0
    for i in range(m - n, m + 1):
        if i + n > m:
            answer += 1
    for i in range(m + 1, n + m):
        answer += 1
    return answer