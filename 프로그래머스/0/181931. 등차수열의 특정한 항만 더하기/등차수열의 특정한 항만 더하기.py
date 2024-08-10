def solution(a, d, included):
    return sum([i * j for i, j in zip([a + i * d for i in range(0, len(included))], included)])