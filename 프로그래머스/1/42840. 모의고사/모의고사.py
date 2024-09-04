def solution(answers):
    l = len(answers)
    a = [1,2,3,4,5] * (l // 5) + [1,2,3,4,5][: (l% 5)]
    b = [2,1,2,3,2,4,2,5] * (l // 8) + [2,1,2,3,2,4,2,5][:(l%8)]
    c = [3,3,1,1,2,2,4,4,5,5] * (l // 10) + [3,3,1,1,2,2,4,4,5,5][:(l%10)]
    answer = []
    result = [0,0,0]
    for i, j in enumerate(answers):
        if j == a[i]:
            result[0] += 1
        if j == b[i]:
            result[1] += 1
        if j == c[i]:
            result[2] += 1
    
    for i, j in enumerate(result):
        if max(result) == j:
            answer.append(i + 1)
    return answer