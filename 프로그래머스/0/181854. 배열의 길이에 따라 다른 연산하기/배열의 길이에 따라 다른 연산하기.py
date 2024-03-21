def solution(arr, n):
    return [num + n*((len(arr)+i)%2) for i, num in enumerate(arr)] 