s = input().upper()
count_dic = {}

for i in s:
    count_dic[i] = count_dic.get(i, 0) + 1

max_count = max(count_dic.values())
most_common = [key for key, value in count_dic.items() if value == max_count]

print("?") if len(most_common) > 1 else print(most_common[0])