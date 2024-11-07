def solution(want, number, discount):
    answer = 0

    # 사려는 제품이 존재하는지 확인
    for i, j in enumerate(want):
        if number[i] != 0 and j not in discount:
            return 0
    
    for i in range(len(discount)):
        a = []
        lst = discount[i:i+10]
        
        for j, k in enumerate(want):
            if number[j] != lst.count(k):
                break
            else:
                a.append(lst.count(k))
        if a == number:
            answer += 1

    return answer