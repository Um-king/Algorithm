def solution(l, r):
    return [i for i in range(l, r + 1) if not str(i).replace('0', '').replace('5', '')] or [-1]