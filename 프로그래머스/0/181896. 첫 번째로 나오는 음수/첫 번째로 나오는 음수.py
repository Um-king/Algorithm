def solution(num_list):
    return ([i for i, j in enumerate(num_list) if j < 0] or [-1])[0]