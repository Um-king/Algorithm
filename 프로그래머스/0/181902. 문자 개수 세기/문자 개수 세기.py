def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        answer[ord(i) - 65 if i.isupper() else ord(i) - 71] += 1
    return answer