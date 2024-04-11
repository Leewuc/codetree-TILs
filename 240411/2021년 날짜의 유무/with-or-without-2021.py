def date(a,b):
    if a in [1,3,5,7,8,10,12] and b <= 31:
        print("Yes")
    elif a in [4,6,9,11] and b <= 30:
        print("Yes")
    elif a == [2] and b <= 28:
        print("Yes")
    else:
        print("No")
n,m = list(map(int,input().split()))
date(n,m)