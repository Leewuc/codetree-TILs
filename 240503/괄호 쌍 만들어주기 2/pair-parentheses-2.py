a = input()
cnt = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[i+1] == '((' and a[j]+a[j-1] == '))':
            cnt += 1
print(cnt)