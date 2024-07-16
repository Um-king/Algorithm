# def solution(num_str):
#     return sum([int(i) for i in num_str])


# 문자열은 이미 리스트이기에 위처럼 list로 변환 안해도 된다.
def solution(num_str):
    return sum(map(int, list(num_str)))