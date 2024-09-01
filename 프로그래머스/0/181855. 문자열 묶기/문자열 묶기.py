def solution(strArr):
    dic = {}
    for i in strArr:
        length = len(i)
        if length in dic:
            dic[length] += 1
        else:
            dic[length] = 1
    # 가장 큰 value를 가진 key를 찾고, value가 같다면 key가 큰 것을 선택
    # 여기서 x는 키값
    return max(dic.values())