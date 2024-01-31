n = int(input())
sum = 0
for i in range(n):
    n1 = int(input())
    if(n1 % 2 == 1 and n1 % 3 == 0):
        sum += n1
print(sum)