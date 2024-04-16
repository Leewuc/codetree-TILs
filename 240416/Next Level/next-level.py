class lev:
    def __init__(self,iid,leve):
        self.iid = iid
        self.leve = leve
a,b = input().split()
lee = lev(a,b)
print("user codetree lv 10")
print(f"user {lee.iid} lv {lee.leve}")