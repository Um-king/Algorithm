def solution(number, limit, power):
    answer = []

    # 1을 포함해야하는 약수를 구하는 방법
    for i in range(1, number + 1):
        numbers = []
        for j in range(1, int(i**0.5) + 1):  # 제곱근까지만 확인
            if i % j == 0: 
                numbers.append(j)
                if j != i // j:  # 제곱이 아닌 경우에만 추가
                    numbers.append(i // j)
        answer.append(len(numbers))

    return sum([power if i > limit else i for i in answer])