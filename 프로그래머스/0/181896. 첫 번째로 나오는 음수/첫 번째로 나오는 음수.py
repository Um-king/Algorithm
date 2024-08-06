def solution(num_list):
    return num_list.index(next(filter(lambda x : x < 0, num_list))) if sum(map(lambda x : x < 0, num_list)) > 0 else -1