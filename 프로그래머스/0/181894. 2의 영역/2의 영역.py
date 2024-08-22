def solution(arr):
    lst = [i for i,j in enumerate(arr) if j==2]
    return arr[lst[0]:lst[-1]+1] if lst else [-1]