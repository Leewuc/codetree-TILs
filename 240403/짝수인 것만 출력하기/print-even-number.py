n = int(input())
numLst = list(map(int, input().split()))

[
    print(ele, end = ' ')
    for ele in numLst
    if ele % 2 == 0
]