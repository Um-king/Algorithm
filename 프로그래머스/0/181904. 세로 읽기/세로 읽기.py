def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string) // m):
        answer += my_string[i*m:i*m+m][c - 1]
    return answer