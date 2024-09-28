dice = list(map(int, input().split()))

max_count = 0
max_value = 0

for i in range(1, 7):
    count = dice.count(i)

    if max_count < count:
        max_count = count
        max_value = i
    
if max_count == 3:
    print(10000 + max_value * 1000)
elif max_count == 2:
    print(1000 + max_value * 100)
elif max_count == 1:
    print(100 * max(dice))