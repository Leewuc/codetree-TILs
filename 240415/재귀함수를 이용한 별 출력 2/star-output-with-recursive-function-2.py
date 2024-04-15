def star(n):
    if n == 0:
        return 
    print("* "*n)
    star(n-1)
def star2(n):
    if n == 0:
        return
    star2(n-1)
    print("* "* n)
    
n = int(input())
star(n)
star2(n)