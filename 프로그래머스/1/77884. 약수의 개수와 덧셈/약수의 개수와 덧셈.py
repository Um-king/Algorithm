def solution(left, right):
    # answer = 0
    # for i in range(left, right + 1):
    #     cnt = 0
    #     for j in range(1, i +1):
    #         if i % j == 0:
    #             cnt+=1
    #     answer += i if cnt % 2 == 0 else -i
    # return answer
    return sum(n if (n ** 0.5) % 1 else -n for n in range(left, right + 1))