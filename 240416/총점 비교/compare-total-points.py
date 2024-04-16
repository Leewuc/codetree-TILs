n = int(input())
class exam:
    def __init__(self,name,a,b,c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
ex = []
for _ in range(n):
    n,x,y,z = list(input().split())
    ex.append(exam(n,int(x),int(y),int(z)))
ex.sort(key=lambda x : x.a + x.b + x.c)
for exa in ex:
    print(exa.name, exa.a, exa.b, exa.c)