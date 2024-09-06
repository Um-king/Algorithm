def solution(brown, yellow):
    answer = []
    number = brown+yellow
    # 전체 약수를 구함
    for i in range(1, number+1):
        if number%i == 0:
            answer.append(i)

    for h in answer:
        w = number // h
        if (w-2)*(h-2) == yellow:
            return [w, h]
