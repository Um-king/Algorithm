def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += i
        
        elif i.isupper():
            print(ord(i), ord('A'))
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            print(ord(i), ord('a'))
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))

    return answer