def solution(n):
    answer = [n]
    while answer[-1] != 1:
        answer.append(3 * n + 1 if n % 2 else n / 2)
        n = answer[-1]

    return answer