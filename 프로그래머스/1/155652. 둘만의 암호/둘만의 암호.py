def solution(s, skip, index):
    lst = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    return ''.join([lst[(lst.index(i) + index) % len(lst)] for i in s])