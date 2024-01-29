def solution(sides):
    l = sorted(sides, reverse=True)
    return 1 if l[0] < l[1] + l[2] else 2