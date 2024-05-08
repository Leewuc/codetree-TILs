from sys import stdin
n, k = list(map(int, stdin.readline().split()))
arr = [stdin.readline().split() for _ in range(n)]

base = [0]*(10000+10000+1) #최대 위치+최대 길이, 범위의 조건나누기 싫어서!
k = k+1 #[1,7]은 구간은 6이지만 범위는 [1,7]로 양쪽 다 포함 총 7개의 숫자!

scale = 0
for num, value in arr:
    base[int(num)] = 1 if value == "G" else 2
    scale = max(scale, int(num))

# print(base[:20])

result = 0
for i in range(1, k+1):
    result += base[i]
# print(result)

cur = result
for i in range(2, scale+1): #2~scale까지 #처음은 이미 봄!
    cur = cur - base[i-1] + base[i+k-1] #k가 1시 i를 더해야 함!
    result = max(result, cur)
print(result)