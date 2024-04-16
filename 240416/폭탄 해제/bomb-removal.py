class bomb:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second
co,col,sec = tuple(input().split())
bomb_a = bomb(co,col,int(sec))
print(f"code : {bomb_a.code}\ncolor : {bomb_a.color}\nsecond : {bomb_a.second}")