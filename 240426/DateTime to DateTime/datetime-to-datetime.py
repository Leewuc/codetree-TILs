a,b,c = map(int,input().split())
if a < 11 or b < 11 or c < 11:
    print(-1)
d = (a - 11) * 1440
d += ((b-11)*60)
d += (c-11)
print(d)