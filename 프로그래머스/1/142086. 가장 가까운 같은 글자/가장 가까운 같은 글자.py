def solution(s):
    count = 0
    l = []
    for i in s:
        s_slice = s[:count]
        lst = list(filter(lambda x: s_slice[x] == i, range(len(s_slice))))
        if len(lst) != 0:
            l.append(count - lst[len(lst)-1])
        else:
            l.append(-1)
        count += 1
    return l