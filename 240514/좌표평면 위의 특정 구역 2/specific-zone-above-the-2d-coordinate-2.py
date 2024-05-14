import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int,input().split())))
xl,yl,rec = [],[],[]
for x,y in arr:
    xl.append(x)
    yl.append(y)
for i in range(n):
    txl = list(xl)
    tyl = list(yl)
    del txl[i]
    del tyl[i]
    rec.append((max(txl)-min(txl)) * (max(tyl)-min(tyl)))
print(min(rec))