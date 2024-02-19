def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr) == 1 else arr