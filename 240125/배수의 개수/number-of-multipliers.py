cnt,cnt1 = 0,0
for _ in range(10):
    n = int(input())
    if(n % 3 == 0):
        cnt += 1
    if(n%5 == 0):
        cnt1 += 1
print(cnt, cnt1)