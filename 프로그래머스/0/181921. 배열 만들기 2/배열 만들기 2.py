def solution(l, r):
    return [i for i in range(l, r + 1) if not str(i).replace('0', '').replace('5', '')] or [-1]

    # 보편적 답 set을 사용(0과 5가 중복되지 않은 상태에서 뺏을 때 값이 비어있다면 해당 값은 0과 5로만 이루어진것)
    # answer = []
    # for i in range(l, r + 1):
    #     if not set(str(i)) -  set(['0', '5']):
    #         answer.append(i)
    # return answer if answer else [-1]