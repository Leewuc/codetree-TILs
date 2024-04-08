n1,n2 = map(str,input().split())
nn1 = len(n1)
nn2 = len(n2)
if nn1 == nn2:
    print("same")
elif nn1 > nn2:
    print(f"{n1} {nn1}")
else:
    print(f"{n2} {nn2}")