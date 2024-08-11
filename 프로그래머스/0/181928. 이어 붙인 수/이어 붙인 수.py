def solution(num_list):
    return sum((int(''.join([str(i) for i in num_list if i % 2 == 0])), int(''.join([str(i) for i in num_list if i % 2 != 0]))))