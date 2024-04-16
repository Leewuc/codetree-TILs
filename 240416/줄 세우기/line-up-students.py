n = int(input())
class student:
    def __init__(self,height,weight,num):
        self.height = height
        self.weight = weight
        self.num = num
stu = []
for _ in range(n):
    h,w = list(input().split())
    stu.append(student(int(h),int(w),_))
stu.sort(key=lambda x: (-x.height,-x.weight,x.num))
for stud in stu:
    print(stud.height, stud.weight,stud.num+1)