class priv:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
person = []
for _ in range(5):
    n,h,w = list(input().split())
    person.append(priv(n,int(h),float(w)))
person.sort(key=lambda x: x.name)
print("name")
for per1 in person:
    print(per1.name, per1.height, per1.weight)
person.sort(key=lambda y: -y.height)
print()
print("height")
for per2 in person:
    print(per2.name, per2.height, per2.weight)