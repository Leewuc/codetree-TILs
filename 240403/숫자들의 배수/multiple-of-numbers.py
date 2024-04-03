n=int(input())
multiples=1
five=[]
while True:
    result = n*multiples
    print(result, end=' ')
    multiples+=1
    if result%5==0:
        five.append(result)
    if len(five)==2:
        break