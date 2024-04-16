n = int(input())

class Distance:
    def __init__(self, x, y, number, xy):
        self.x = x
        self.y= y
        self.number =number
        self.xy= xy


distances = []
for i in range(n):
    x, y = tuple(map(int, input().split()))
    if x < 0:
        x += 2*(-x)
    if y < 0:
        y += 2*(-y)
    xy = x+y
    distances.append(Distance(x, y, i+1, xy))

distances.sort(key= lambda x: (x.xy, x.number))

for dis in distances:
    print(dis.number)