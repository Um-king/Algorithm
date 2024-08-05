def solution(absolutes, signs):
    return sum(map(lambda x : x[0] if x[1] else -x[0], zip(absolutes, signs)))


# def solution(absolutes, signs):
#     return sum(map(lambda x : absolutes[x] if signs[x] else -absolutes[x], range(len(absolutes))))