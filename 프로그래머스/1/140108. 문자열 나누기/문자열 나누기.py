def solution(s):
    answer, cnt1, cnt2, index = 0, 0, 0, 0
    w1, w2 = s[0], ""

    while len(s) > 1:
        if index == len(s):
            return answer + 1
        if w1 == s[index]:
            cnt1 += 1
        else:
            cnt2 += 1
        
        index += 1

        if cnt1 == cnt2:
            s = s[index:]
            cnt1, cnt2, index = 0, 0, 0
            if len(s) > 1:
                w1 =  s[index]
            answer += 1

    return answer + len(s)