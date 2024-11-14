n = int(input())
lst = map(int, input().split())
cnt = 0

for i in lst:
    count = 0

    if i < 2:
        continue
    
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        cnt += 1
    
print(cnt)
