def solution(keymap, targets):
    answer = []
    d = {}

    for word in keymap:
        for i, j in enumerate(word):
            if j in d and i+1 > d[j]:
                continue
            d[j] = i+1
    
    for i in targets:
        num = 0
        for j in i:
            if j in d:
                num += d[j]
            else:
                num = -1
                break
                
        answer.append(num)
    return answer