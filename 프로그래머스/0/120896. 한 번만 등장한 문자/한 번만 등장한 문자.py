def solution(s):
    set_data = set(s)
    return ''.join(sorted([i for i in set_data if s.count(i) == 1]))