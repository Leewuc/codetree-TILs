n = int(input())
class exam:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
ex = []
for _ in range(n):
    n,k,e,m = list(input().split())
    ex.append(exam(n,int(k),int(e),int(m)))
ex.sort(key=lambda x: (-x.kor,-x.eng,-x.math))
for exa in ex:
    print(exa.name, exa.kor, exa.eng, exa.math)