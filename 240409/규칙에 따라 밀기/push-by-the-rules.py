s = input()
op = input()
for i in op:
    if i == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]

print(s)