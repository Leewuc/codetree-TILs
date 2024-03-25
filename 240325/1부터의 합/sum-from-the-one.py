n = int(input())
prod = 0
ans = 0
for i in range(1,101):
    prod += i
    if(prod >= n):
        ans = i
        break
print(ans)