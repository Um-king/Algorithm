n, m = map(int, input().split())
num_list = input().split()
l = filter(lambda x: int(x)<m, num_list)
print(' '.join(l))