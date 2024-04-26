m1, d1, m2, d2 = map(int, input().split())

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_days = d2 - d1 + 1
for month in range(m1, m2):
    total_days += days_in_month[month]

print(total_days)