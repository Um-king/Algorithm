def solution(food):
    answer = []
    for i, j in enumerate(food):
        for k in range(j // 2):
            answer.append(str(i))
    return ''.join(answer + ['0'] + answer[::-1])