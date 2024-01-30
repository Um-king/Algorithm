def solution(n): # 나눴을때 0인 것들(약수)
    return len(list(filter(lambda x : n % (x + 1) == 0, range(n))))