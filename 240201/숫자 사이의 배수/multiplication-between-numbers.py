a,b = map(int,input().split())
sum = 0
mean = 0
cnt = 0
for i in range(a,b+1):
    if(i % 5 == 0 or i  % 7 == 0):
        sum += i
        cnt += 1
        mean = round(sum / cnt,1)
print(sum, mean)