def solution(arr1, arr2):
    return [[n + m for n,m in zip(i, j)] for i,j in zip(arr1, arr2)]