n = int(input())
class student:
    def __init__(self,tall,weight,num):
        self.tall = tall
        self.weight = weight
        self.num = num
stud = []
for _ in range(n):
    h,w = list(input().split())
    stud.append(student(h,w,_))
stud.sort(key=lambda x: (x.tall,x.weight,x.num))
for su in stud:
    print(su.tall, su.weight, su.num+1)