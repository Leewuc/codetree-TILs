class gog:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
x,y,z = input().split()
gg = gog(x,y,z)
print(f"secret code : {gg.a}\nmeeting point : {gg.b}\ntime : {gg.c}")