from functools import reduce

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else reduce(lambda x, y : x * y, num_list)


# reduce 함수는 시퀀스(리스트 등)의 요소들을 누적하여 단일 결과를 만드는 함수입니다. 
# reduce 함수는 다음과 같은 원리로 동작합니다:

# 1. 시퀀스의 첫 두 요소를 가져와서 주어진 함수를 적용합니다.
# 2. 그 결과와 다음 요소를 가져와서 주어진 함수를 다시 적용합니다.
# 3. 시퀀스의 모든 요소에 대해 이 과정을 반복하여 최종 결과를 얻습니다.