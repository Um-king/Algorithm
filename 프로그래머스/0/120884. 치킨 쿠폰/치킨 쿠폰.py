def solution(chicken):
    answer = 0
    while chicken >= 10:
        result, mod = divmod(chicken, 10)
        answer += result
        chicken = result + mod
    return answer