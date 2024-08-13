def solution(n, control):
    num = {'w':1, 's':-1, 'd':10, 'a':-10}
    return n + sum([num[i] for i in control])