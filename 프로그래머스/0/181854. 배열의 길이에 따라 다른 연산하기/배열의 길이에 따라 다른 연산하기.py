def solution(arr, n):
    if len(arr) % 2 == 0:
        return [j + n if i % 2 != 0 else j for i, j in enumerate(arr)]
    else:
        return [j + n if i % 2 == 0 else j for i, j in enumerate(arr)]