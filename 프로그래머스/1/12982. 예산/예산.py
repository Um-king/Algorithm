def solution(d, budget):
    d = sorted(d)
    for i, j in enumerate(d):
        budget -= j
        if budget < 0:
            return i
    return len(d)