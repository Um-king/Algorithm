def solution(s):
    zero_cnt = 0
    num_cnt = 0

    while s != "1":
        zero_cnt += s.count("0")
        num_cnt += 1
        s = bin(s.replace("0","").count("1"))[2:]
        
    return [num_cnt, zero_cnt]