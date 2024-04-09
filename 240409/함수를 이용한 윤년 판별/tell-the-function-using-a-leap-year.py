def yoon(n):
    yy = False
    if n % 4 != 0 or (n % 100 and n % 400 != 0 ):
        yy = "true"
    else:
        yy = "false"
    return yy
n = int(input())
print(yoon(n))