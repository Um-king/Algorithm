def solution(num_list):
    n1 = sum(num_list[::2])
    n2 = sum(num_list) - n1
    return n2 if n1 < n2 else n1