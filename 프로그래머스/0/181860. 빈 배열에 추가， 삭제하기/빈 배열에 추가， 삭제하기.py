def solution(arr, flag):
    answer = []
    for i, j in enumerate(flag):
        if j:
            for k in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            for q in range(arr[i]):
                answer.pop()
    return answer    