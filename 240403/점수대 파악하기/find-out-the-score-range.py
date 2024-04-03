arr = list(map(int,input().split()))
count = [0,0,0,0,0,0,0,0,0,0]

for i in arr :
    for j in range(9,-1,-1) :
        if int(i/10) == (j+1) :
            count[j] += 1
        elif i == 0:
            break


for i in range(0,10) :
    print(f"{100-(i*10)} - {count[9-i]}")