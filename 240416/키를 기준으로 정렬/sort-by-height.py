n = int(input())
class student:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age
sor = []
for _ in range(n):
    n,h,a = list(input().split())
    sor.append(student(n,h,a))
sor.sort(key=lambda x: x.height)
for ss in sor:
    print(ss.name, ss.height, ss.age)