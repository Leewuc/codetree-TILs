n = int(input())
count = 0
while n > 1:
    n = n // (count + 1)
    count += 1

print(count)