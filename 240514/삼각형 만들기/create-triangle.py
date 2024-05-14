n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

def pall(x,y,z):
    x1,y1 = x
    x2,y2 = y
    x3,y3 = z
    if (x1==x2 or x2 == x3 or x1 == x3) and (y1==y2 or y2==y3 or y1 == y3):
        return True
    else:
        return False
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x,y,z = arr[i],arr[j],arr[k]

            if pall(x,y,z):
                x1,y1 = x
                x2,y2 = y
                x3,y3 = z
                xmin = min(x1,x2,x3)
                xmax = max(x1,x2,x3)
                ymin = min(y1,y2,y3)
                ymax = max(y1,y2,y3)
                diff = ((xmax-xmin) * (ymax-ymin))
                cnt = max(cnt,diff)
print(cnt)