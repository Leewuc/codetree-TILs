n = input()
n1 = input()
cnt = 0
for i in range(len(n)):
    if n[i] == n1:
        cnt += 1
print(cnt)