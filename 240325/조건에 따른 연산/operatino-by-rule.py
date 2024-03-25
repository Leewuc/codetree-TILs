n = int(input())
for cnt in range(1000):
    if n >= 1000:
        print(cnt)
        break
    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = n * 2 + 2
else:
    print(-1)