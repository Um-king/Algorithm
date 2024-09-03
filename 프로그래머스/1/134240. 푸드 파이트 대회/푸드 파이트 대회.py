def solution(food):
    answer = ""
    for i, j in enumerate(food[1:]):
        # 해당 인덱스가 어차피 1,2,3 계산된 것이니깐, 인덱스에 해당 음식 개수의 반개를 곱해서 문자열의 개수를 만든다..!
        answer += (str(i+1)) * (j // 2)
    return answer + "0" + answer[::-1]