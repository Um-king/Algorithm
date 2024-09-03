def solution(babbling):
    answer = 0
    for i in babbling:
        if len((i.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ")).split()) == 0:
            answer += 1
    return answer