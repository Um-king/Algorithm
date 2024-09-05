def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            del stack[-4:] # 스택의 내용을 지우면 된다. -> 그럼 원 리스트를 건들 필요 없음..!
    return answer