def solution(a, b):
    if a == b:
        return a

    l = sorted([a, b])
    return sum([i for i in range(l[0], l[len(l) - 1] + 1)])