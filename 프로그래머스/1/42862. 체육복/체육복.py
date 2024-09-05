def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()

    for i in range(1, n + 1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    for i in range(1, n+1):
        if i not in lost:
            answer += 1
        elif i in lost:
            for j in reserve:
                if i + 1 == j or i - 1 == j:
                    answer += 1
                    reserve.remove(j)
                    break
    return answer