n = input()
n1 = n.split()
a = n1[0]
a1 = int(n1[1])
if a == 'A':
    for i in range(1,a1+1):
        print(i,end=' ')
        i += 1
else:
    for i in range(a1,1+1):
        print(i,end=' ')
        i -= 1