n = input()
if n[-1] in n:
    print(n.index(n[-1]))
else:
    print("No")