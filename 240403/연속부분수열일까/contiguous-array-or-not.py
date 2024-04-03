from sys import stdin
n1, n2 = list(map(int, stdin.readline().split()))
arrA = list(map(int, stdin.readline().split()))
arrB = list(map(int, stdin.readline().split()))
key = False #n2가 n1보다 크다면 for문이 돌지 않으므로
for i in range(n1-n2+1): #수열A에서 처음부터 n1-n2까지 봄
    key = True
    for j in range(n2): #수열 B를 순차적으로 탐색, 다르면 False가 되고 멈춤
        if arrA[i+j] != arrB[j]:
            key = False
            break
    if key: #다 돌았고 맞음
        break
if key:
    print("Yes")
else:
    print("No")