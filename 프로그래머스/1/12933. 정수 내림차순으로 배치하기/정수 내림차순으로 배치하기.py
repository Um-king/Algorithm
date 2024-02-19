def solution(s):
    return int(''.join(sorted(str(s), reverse=True)))