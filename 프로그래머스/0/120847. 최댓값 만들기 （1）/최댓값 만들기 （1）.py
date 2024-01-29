def solution(numbers):
    l = sorted(numbers, reverse=True)
    return l[0] * l[1]