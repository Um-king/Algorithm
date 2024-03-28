def solution(num_list, n):
    if len(num_list) % n != 0:
        return

    result = []
    lst = []
    for i in num_list:
        lst.append(i)
        if len(lst) == n:
            result.append(lst)
            lst = []
    return result