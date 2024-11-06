n ,k = map(int, input().split())
lst = map(int, input().split())

print(sorted(lst, reverse=True)[k-1])