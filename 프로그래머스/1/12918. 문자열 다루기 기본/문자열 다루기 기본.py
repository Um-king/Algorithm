def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    return sum(list(map(lambda x: x.isdigit(), s))) == len(s)