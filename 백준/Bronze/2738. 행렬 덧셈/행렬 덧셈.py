n, m = map(int, input().split())
lst1 = []  
lst2 = []  

for _ in range(n):
    lst1.append(list(map(int, input().split())))

for _ in range(n):
    lst2.append(list(map(int, input().split())))

for i in range(n):
    result_row = [lst1[i][j] + lst2[i][j] for j in range(m)]
    print(" ".join(map(str, result_row)))