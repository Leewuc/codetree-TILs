def flow(n):
    if n == 0:
        return
    print(n,end=" ")
    flow(n-1)
def flow2(n):
    if n == 0:
        return
    flow2(n-1)
    print(n,end = " ")
n = int(input())
flow(n)
flow2(n)