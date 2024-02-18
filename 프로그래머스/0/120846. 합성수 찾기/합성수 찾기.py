def solution(n):
    lst = []
    for i in range(1, n + 1):
        l = []
        for j in range(1, i):
            if i % j == 0:
                l.append(j)
        lst.append(l)
    return sum(map(lambda x: len(x) > 1 ,lst))