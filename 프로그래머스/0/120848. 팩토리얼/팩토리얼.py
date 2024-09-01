def solution(n):
    cnt = 1
    answer = 1
    while cnt < 11:
        answer *= cnt
        if answer > n:
            return cnt - 1
        cnt += 1
    return 10