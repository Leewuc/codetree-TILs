def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return "true"
    return "false"

y = int(input())
print(is_leap_year(y))