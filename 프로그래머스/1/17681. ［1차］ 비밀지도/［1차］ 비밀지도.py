def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 정수끼리 비트 연산을 통해 이진수로 변환하여 계산 후 다시 정수로 반환하는 개념
        result = bin(arr1[i] | arr2[i])[2:]
        answer.append(("0" * (n - len(result))) + result)

    return [i.replace("1", "#").replace("0", " ") for i in answer]