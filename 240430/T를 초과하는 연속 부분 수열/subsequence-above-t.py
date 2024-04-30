n,t = tuple(map(int,input().split()))
new_n =list(map(int,input().split()))
cnt = 0
ans = 0
for i in range(n):
    if new_n[i] > new_n[i-1] and new_n[i] > t:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans,cnt)
print(ans-1)