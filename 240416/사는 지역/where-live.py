class local:
    def __init__(self,name,number,loc):
        self.name = name
        self.number = number
        self.loc = loc
n = int(input())
peop = []
for _ in range(n):
    x,y,z = tuple(input().split())
    peop.append(local(x,y,z))
ll = [person.name for person in peop]
ll.sort()
for i in range(n):
    if peop[i].name == ll[n-1]:
        print(f"name {peop[n-1].name}")
        print(f"addr {peop[n-1].number}")
        print(f"city {peop[n-1].loc}")