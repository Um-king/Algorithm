n = input()
print(''.join(sorted(n, key = lambda x:int(x), reverse=True)))