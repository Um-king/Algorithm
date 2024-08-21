def solution(arr, idx):
    return -1 if sum(arr[idx:]) < 1 else [i for i, j in enumerate(arr) if i >= idx and arr[i] == 1][0]