def solution(i, j, k):
    return sum(map(lambda x: str(x).count(str(k)), range(i, j+1)))