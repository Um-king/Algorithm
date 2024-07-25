# def solution(array, n):
#     # 대상, key=함수: 대상에 대해서 해당 함수 적용, 함수내 두번째 인자: 정렬 순서 
#     # abs(x-n)가 같을 때 x값이 작은 순으로 정렬
#     return min(array, key = lambda x: (abs(x-n),  x-n)) 

def solution(array, n):
    # 대상, key=함수: 대상에 대해서 해당 함수 적용, 함수내 두번째 인자: 정렬 순서 
    # abs(x-n)가 같을 때 x값이 작은 순으로 정렬
    return sorted(array, key = lambda x: (abs(x-n),  x-n))[0]
