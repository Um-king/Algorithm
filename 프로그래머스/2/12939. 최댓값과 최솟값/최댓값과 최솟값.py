def solution(s):
    l = sorted(list(map(int, (s.split()))))
    return ' '.join([str(l[0]), str(l[-1])])