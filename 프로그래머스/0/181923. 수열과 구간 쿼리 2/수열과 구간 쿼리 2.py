def solution(arr, queries):
    result_lst = []
    for i,j,k in queries:
        lst = [n for n in arr[i : j + 1] if n > k]
        result_lst.append(min(lst)) if lst else result_lst.append(-1)
    return result_lst