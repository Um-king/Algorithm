def solution(k, score):
    result = [] # 명예의 전당
    answer = [] # 발표 점수

    for i in score:
        result.append(i)
        if len(result) > k:
            result.remove(min(result))
        answer.append(min(result))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))