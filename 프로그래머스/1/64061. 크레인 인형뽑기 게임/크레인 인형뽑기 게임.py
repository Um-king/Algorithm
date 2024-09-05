def solution(board, moves):
    answer = 0
    box = []
    stack = []
    for i in range(len(board)):
        b = []
        for j in range(len(board)):
            if board[j][i] != 0:
                b.append(board[j][i])
        box.append(b)
   
    for i in moves:
        if not box[i-1]:
            continue
        if not stack or stack[-1] != box[i-1][0]:
            stack.append(box[i-1][0])
        else:
            stack.pop()
            answer += 1
        box[i-1].pop(0)        
    return answer * 2
