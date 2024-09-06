def solution(k, tangerine):
    answer = 0
    total = 0
    d = {}
    for i in tangerine:
        if i in d: 
            d[i] += 1
        else:
            d[i] = 1
    l = sorted(d.items(), key=lambda x:x[1], reverse=True)

    for i, j in l:
        if j >= k:
            return 1
        total += j
        answer += 1
        if total >= k:
            return answer
    return answer