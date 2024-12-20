def solution(lottos, win_nums):

    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    zero = lottos.count(0)

    min_num = len([i for i in lottos if i in win_nums])   
    max_num = min_num + zero

    return [rank[max_num], rank[min_num]]