def solution(k, score):
    result = [] # 명예의 전당
    answer = [] # 최하위 점수
    for i in score:
        result.append(i)
        result.sort(reverse=True)

        if len(result)> k:
            result.pop() # 최하위 점수를 제거
        
        answer.append(result[-1])
    
    return answer