n=int(input())
arr=list(map(int, input().split()))
#k의 최대는 100
k_max=0
for k in range(1, 101):
    #두 수를 수열에서 뽑기
    cnt=0
    for i in range(n):
        for j in range(i, n): #####이부분을 i+1로 바꾸어야 맞았다고 뜹니다#####
            if (arr[i]+arr[j])/2==k:
                cnt+=1
    k_max=max(k_max, cnt)
print(k_max)