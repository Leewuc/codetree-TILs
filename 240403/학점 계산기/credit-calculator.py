n = int(input())
arr = list(map(float,input().split()))
mea = 0
su = sum(arr)
mea = su/n
print(f"{mea:.1f}")
if mea >= 4.0:
    print("Perfect")
elif mea >= 3.0 and 4.0 > mea:
    print("Good")
else:
    print("Poor")