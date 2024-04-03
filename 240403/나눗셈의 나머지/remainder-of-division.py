a, b = map(int, input().split())

remainders_count = {}
while a > 1:
    q, r = divmod(a, b)
    a = q
    if r in remainders_count:
        remainders_count[r] += 1
    else:
        remainders_count[r] = 1

total = sum([count**2 for count in remainders_count.values()])
print(total)