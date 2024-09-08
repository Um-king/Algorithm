def solution(arr):
    row, col = len(arr), len(arr[0])
    if row > col:
        for i in arr:
            for _  in range(row-col):
                i.append(0)
    else:
        for _ in range(col-row):
            arr.append([0] * col)
    return arr