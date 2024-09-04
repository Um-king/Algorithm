def solution(n):
    # n개의 숫자를 생성한다
    nums = set(i for i in range(2, n + 1))

    for i in range(2, n + 1): 
        # 차집합을 통해 소수의 배수들을 전부 제거한다.
        nums -= set(j for j in range(i * 2, n + 1, i))

    return len(nums)