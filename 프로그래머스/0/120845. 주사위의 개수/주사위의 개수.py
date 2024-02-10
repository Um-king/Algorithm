def solution(box, n):
    return eval('*'.join([str(x // n) for x in box]))