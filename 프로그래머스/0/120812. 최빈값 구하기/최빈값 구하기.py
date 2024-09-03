def solution(array):
    d = {}
    for i in array:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    answer = sorted(d.items(), key=lambda x:x[1], reverse=True)
    return -1 if len(answer) > 1 and answer[0][1] == answer[1][1] else answer[0][0]