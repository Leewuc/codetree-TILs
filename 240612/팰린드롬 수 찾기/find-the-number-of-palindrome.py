x,y = map(int,input().split())
cnt = 0
for i in range(x,y+1):
    i_1 = str(i)
    i_2 = str(i)[::-1]
    if i_1 == i_2:
       cnt += 1
print(cnt)