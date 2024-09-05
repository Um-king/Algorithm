def solution(board, h, w):
    
    # dx = [-1, 0, 1, 0]
    # dy = [0, -1, 0, 1]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    length = len(board)
    answer = 0
    
    for i in range(4):
        nx, ny = w+dx[i], h+dy[i]

        if nx < 0 or nx >= length or ny < 0 or ny >= length:
            continue

        if board[h][w] == board[ny][nx]:
            answer += 1
    return answer