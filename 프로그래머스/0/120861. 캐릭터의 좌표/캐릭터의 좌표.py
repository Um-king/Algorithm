def solution(keyinput, board):
    x_max, y_max = board[0] // 2, board[1] // 2
    x, y = 0, 0

    for i in keyinput:
        if i == "up" and y < y_max:
            y += 1
        elif i == "down" and y > -y_max:
            y -= 1
        elif i == "left" and x > -x_max:
            x -= 1
        elif i == "right" and x < x_max:
            x += 1
    return [x, y]        