arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]==0:
        break
    elif arr[i]%2==1:
        print(arr[i]+3,end=' ')
    else:
        print(arr[i]//2,end=' ')