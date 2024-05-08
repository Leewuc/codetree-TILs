from sys import stdin
n = int(stdin.readline())
#세로1,가로3인 격자
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

ans = 0

#난 매번 체크하고 싶지 않아! 역순으로 최댓값을 미리 구하면서 진행
result = 0
for i in range(n-1,-1,-1):
    cur = 0
    for j in range(n-3,-1,-1): #들여쓰기 ㅠㅜ j돌때마다 체크해야 됨!
        cur = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        # if cur > result:
            # print("초기 역순 탐색 중첩", i, j)
        result = max(cur, result)
        if in_range(i, j-3):
            # if ans < result + arr[i][j-3]+arr[i][j-2]+arr[i][j-1]:
                # print("같은 행", i, j-3)
            ans = max(ans, result + arr[i][j-3]+arr[i][j-2]+arr[i][j-1]) #겹치지 않는 행!
        #왼쪽은 다음 칸에서 다시 계산, 하지만 max로 갱신되므로 우측이 최대여도 괜찮음
        if in_range(i-1, j):
            # if ans < result + arr[i-1][j]+arr[i-1][j+1]+arr[i-1][j+2]:
            #     print("바로 위 행", i-1, j, ans, result + arr[i-1][j]+arr[i-1][j+1]+arr[i-1][j+2])
            ans = max(ans, result + arr[i-1][j]+arr[i-1][j+1]+arr[i-1][j+2])
        #마찮가지로 바로 위의 경우 계산, max가 유지되므로 역순으로 max값인 상태에서 가면서 가장 최대 찾음!    

print(ans)