def solution(n, words):
    answer = []
    s = []
    for i, j in enumerate(words):
        if j in s:
            answer.append([(i) % n + 1, i // n + 1])
            break
        
        if len(s) > 0 and s[-1][-1] != j[0]:
            answer.append([(i) % n + 1, i // n + 1])

        s.append(j)

    return answer[0] if answer else [0, 0]