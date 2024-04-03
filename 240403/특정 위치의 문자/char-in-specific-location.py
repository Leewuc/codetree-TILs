n = input()
idx = -1
word = ['L','E','B','R','O','S']
for i , char in enumerate(word):
    if char == n:
        idx = i
if idx == -1:
    print("None")
else:
    print(idx)