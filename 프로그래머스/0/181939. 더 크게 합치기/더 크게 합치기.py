def solution(a, b):
    return int(sorted([str(a) + str(b), str(b) + str(a)], reverse=True)[0])