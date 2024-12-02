n = int(input())
sangeun = set(map(int, input().split()))

m = int(input())
card = list(map(int, input().split()))

result = ['1' if x in sangeun else '0' for x in card]
print(' '.join(result))