def solution(num_list):
    cnt = 0
    for i in num_list:
        j = i
        while j != 1:
            if j % 2 == 0:
                j = j // 2
            else:
                j = (j - 1) // 2
            cnt += 1
    return cnt