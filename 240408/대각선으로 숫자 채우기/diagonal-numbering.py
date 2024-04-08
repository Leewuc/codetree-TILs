n, m = map(int, input().split())
lst = [[0 for _ in range(m+1)] for _ in range(n+1)]
## 0으로 이루어진 (n+1) * (m+1) 개의 칸 생성 

for l in range(n+1):
    lst[l][0] = -1
## 모든 줄의 맨 앞칸 -1로 변경 (0만 아니면 됨)

for c in range(m+1):
    lst[n][c] = -1
## 마지막 줄을 모두 -1로 변경 (0만 아니면 됨)

cnt = 1 ## 입력할 숫자
for i in range(1, m+1):
    cl = i
    rw = 0
    ## 입력을 시작할 포인트 지정 lst[0][i]
    while lst[rw][cl] != -1:
        lst[rw][cl]=cnt
        rw += 1
        cl -= 1
        cnt += 1
##  lst[rw][cl]=cnt 를  rw += 1, cl -= 1, cnt += 1 해가며 lst[rw][cl] != -1일때까지 반복 
for j in range(1, n):
    cl = -1
    rw = j
    ## 입력을 시작할 포인트 지정 lst[j][-1]
    while lst[rw][cl] != -1:
        lst[rw][cl]=cnt
        rw += 1
        cl -= 1
        cnt += 1
##  lst[rw][cl]=cnt 를  rw += 1, cl -= 1, cnt += 1 해가며 lst[rw][cl] != -1일때까지 반복 


for out in range(n):
    print(*lst[out][1:m+1])  
## -1(첫번째cl, 마지막rw) 제외하고 '()', ',' 떼고 출력