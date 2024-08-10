def solution(a, d, included):
    return sum([(a + i * d) * included[i] for i in range(len(included))])