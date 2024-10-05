x = int(input())
score = list(map(int, input().split()))
max_score = max(score)
lst = []
for i in score:
    lst.append(i/max_score * 100)
print(sum(lst) / x)