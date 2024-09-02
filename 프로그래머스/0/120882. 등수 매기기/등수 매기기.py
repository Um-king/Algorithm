def solution(score):
    avg_list = sorted([i + j for i, j in score], reverse=True)
    return [avg_list.index(sum(i)) + 1 for i in score]