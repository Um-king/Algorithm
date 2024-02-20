def solution(arr, divisor):
    l = sorted(list(filter(lambda x: x%divisor == 0, arr)))
    return l if len(l) > 0 else [-1]