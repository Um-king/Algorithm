def solution(numbers):
    l = sorted(numbers)
    return max(l[0] * l[1], l[-1] * l[-2])