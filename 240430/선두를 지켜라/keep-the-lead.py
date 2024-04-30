n,m = tuple(map(int,input().split()))
cnt = 1
a_v = []
b_v = []
for i in range(n):
    v,t = tuple(map(int,input().split()))
    a_v.append(v)
    b_v.append(t)
    if a_v[i] > b_v[i] and a_v[i-1] < b_v[i-1]:
        cnt += 1
    elif a_v[i] < b_v[i] and a_v[i-1] > b_v[i-1]:
        cnt += 1
print(cnt)