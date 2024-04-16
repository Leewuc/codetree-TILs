n = int(input())
class student:
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
stu = []
for _ in range(n):
    n,w,h = list(input().split())
    stu.append(student(n,int(w),int(h)))
stu.sort(key=lambda x: (x.weight,-x.height))
for aa in stu:
    print(aa.name, aa.weight, aa.height)