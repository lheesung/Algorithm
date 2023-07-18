n, m = map(int, input().split())
if n == 1: 
    cnt = 1
elif n == 2: 
    cnt = min(4, (m-1) // 2  +1)
elif m < 7:
    cnt = min(4, m)
else:
    cnt = + m-2
print(cnt)