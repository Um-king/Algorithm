def solution(arr, intervals):
    return [n for i,j in intervals for n in arr[i:j+1]]