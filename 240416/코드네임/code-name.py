class codename:
    def __init__(self,alph,sco):
        self.alph = alph
        self.sco = sco
name = []
for _ in range(5):
    a,b = input().split()
    name.append(codename(a,int(b)))
minsc = 0
for i in range(1,5):
    if name[i].sco < name[minsc].sco:
        minsc += i
print(name[minsc].alph,name[minsc].sco)