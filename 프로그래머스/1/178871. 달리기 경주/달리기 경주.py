def solution(players, callings):
    # 각 플레이어의 현재 인덱스를 저장하는 딕셔너리 생성
    player_index = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        # 불린 플레이어의 현재 인덱스
        current_index = player_index[call]
        
        # 첫번째 플레이어가 불리면 건너뜀
        if current_index == 0:
            continue
        
        # 현재 인덱스와 이전 인덱스에 있는 플레이어 스왑
        previous_index = current_index - 1
        previous_player = players[previous_index]

        # 리스트에서 플레이어 스왑
        players[previous_index], players[current_index] = players[current_index], players[previous_index]
        
        # 딕셔너리에서 인덱스 업데이트
        player_index[call] = previous_index
        player_index[previous_player] = current_index

    return players

# 테스트
solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])


# Q) 질문 참고.. 시간 복잡도에 의한 실행 문제 발생
# 리스트에 있는 변수를 직접 찾아 인덱스를 알아내는 .index() 함수는 시간 복잡도가 O(n)입니다

# 최악의 경우 players의 길이가 50,000 , callings의 길이가 1,000,000 이고 callings에서 항상 꼴등의 이름만 부르는 경우겠죠?

# 이때 다른 로직을 다 제외하고 꼴등의 인덱스 값만 불러오는 코드만 for문으로 실행시켜도 50,000 * 1,000,000 = 50,000,000,000 번의 연산이 필요합니다

# 찾은 인덱스로 꼴등의 이름을 알아내고 꼴등과 꼴등 앞에 있는 선수의 이름을 바꾸는 로직이 추가된다면 시간은 더욱 오래 걸리겠죠

# 다른 방법을 이용하여 선수의 순위를 바꾸는 코드를 작성하셔야 합니다

# 해답
# 본 문제에서는 어떻게 하면 효율적으로 index를 찾을 수 있을 지를 찾는 것이 중요하다고 생각합니다. 저와 같은 경우에는 해시 맵을 사용하여 초기 플레이어의 이름과 등수를 저장하고 관리하였습니다.

# 아마 질문자님께서 시간 초과 오류가 발생한 부분은 players와 callings의 길이가 큰 경우에서 발생한 것으로 보입니다.