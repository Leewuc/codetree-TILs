a,b,c,d = map(int,input().split())
elap_hour = 0
while True:
    if a == c and b == d:
        break
    elap_hour += 1
    b += 1
    if b == 60:
        a += 1
        b = 0
print(elap_hour)