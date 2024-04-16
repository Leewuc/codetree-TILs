class Code:
    def __init__(self, name, score):
        self.name = name
        self.score = score

codes = []
for _ in range(5):
    name, score = tuple(input().split())
    codes.append(Code(name, int(score)))

min_idx = 0
for  i in range(1, 5): # 1 to 4
    if codes[i].score < codes[min_idx].score:
        min_idx = i

print(codes[min_idx].name, codes[min_idx].score)