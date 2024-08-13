def solution(numLog):
    num = {1:'w', -1:'s', 10:'d', -10:'a'}
    return ''.join([num[numLog[i + 1] - numLog[i]] for i in range(len(numLog) - 1)])