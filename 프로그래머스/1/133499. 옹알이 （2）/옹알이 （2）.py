def solution(babbling):
    answer = 0
    # 연속되는 말은 못하니 최소 연속되는 문자로 만들어서 문자열을 바꿔주면 됨
    can_s = ["aya", "ye", "woo", "ma"]
    cant_s = ["ayaaya", "yeye", "woowoo", "mama"]

    for i in babbling:
        for j in cant_s:
            if j in i:
                i = 'x'
        
        for k in can_s:
            i = i.replace(k, ' ')
        i = i.replace(' ', '')
        
        if len(i) == 0:
            answer += 1
    return answer