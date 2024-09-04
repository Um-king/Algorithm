def solution(s, skip, index):
    i, j, n = 0, 0, 0
    alpha = []
    answer = ""
    while i < len(s):
        
        while j < index:
            a = chr((ord(s[i]) - ord('a') + j + 1 + n) % 26 + ord('a'))
            if a in skip:
                n += 1
            else:
                alpha.append(a)
                j += 1

        j, n = 0, 0
        i += 1
        answer += alpha[-1]
    
    return answer