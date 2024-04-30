n = int(input())
cnt = 0
ans = 0
num = 0
for i in range(n):
    new_n = int(input())
    if new_n > num:
        cnt += 1
    else:
        cnt = 1
    ans = max(cnt,ans)
    num = new_n
print(ans)