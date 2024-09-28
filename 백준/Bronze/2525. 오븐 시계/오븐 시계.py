hour, minute = map(int, input().split())
timer = int(input())

t = minute + timer


hour += (t) // 60 
minute = (t) % 60


print(hour % 24, minute)