n = int(input())

odd = 0

even = n+1

for i in range(1, n*2+1):

    if i%2==1:
        odd+=1
        for _ in range(odd):
            print("*", end=" ")
        print()
    else:
        even-=1
        for _ in range(even):
            print("*", end=" ")
        print()