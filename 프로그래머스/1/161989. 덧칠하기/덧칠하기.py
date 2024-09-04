def solution(n, m, section):
    answer = 1
    n = section[0]
    
    for i in section:
        if n + (m-1) < i:
            answer += 1    
            n = i    
            
    return answer