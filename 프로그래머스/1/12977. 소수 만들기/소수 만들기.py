def solution(nums):
    num_list = []
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                num_list.append(nums[i] + nums[j] + nums[k])
    for i in num_list:
        if all(i % j for j in range(2, i)):
            answer.append(i)
    return len(answer)