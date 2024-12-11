lst = []

for _ in range(5):
    lst.append(input())

max_length = max(len(i) for i in lst)
answer = ""

for i in range(max_length):
    for j in lst:
        if i < len(j):
            answer += j[i]
    
print(answer)