lst = list(map(int, input().split()))
num_cnt = 0
num = 0
for i in lst:
    num_value = lst.count(i)
    if num_cnt < num_value:
        num_cnt = num_value
        num = i

print(10000 + num * 1000) if num_cnt == 3 else print(1000 + num * 100) if num_cnt == 2 else print(max(lst) * 100)