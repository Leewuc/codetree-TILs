n = int(input())
string = input()
cnt = 0
for i in range(len(string)):
    for j in range(i+1,len(string)):
        for k in range(j+1,len(string)):
            if string[i] + string[j] + string[k] == 'COW':
                cnt += 1
print(cnt)