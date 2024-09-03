def solution(board):
    check = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    answer = []
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == 1:
                
                for c in check:
                    nx = c[0] + i
                    ny = c[1] + j

                    if (0 <= nx < len(board)) and (0 <= ny < len(board)) and (board[nx][ny] != 1):
                        board[nx][ny] = "X"
    return len([j for i in board for j in i if j == 0])