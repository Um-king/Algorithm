def solution(num, total):
    answer = [i for i in range(-(num // 2), num + total)]
    for i in range(total + num):
        if sum(answer[i:i+num]) == total:
            return answer[i:i+num]