def solution(n):
    lst = ['수', '박']
    return ''.join([lst[i % len(lst)] for i in range(0, n)])