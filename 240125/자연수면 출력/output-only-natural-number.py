a,b = input().split()
a,b = int(a),int(b)
if(a > 0):
    for i in range(0,b,1):
        print(a,end="")
else:
    print("0")