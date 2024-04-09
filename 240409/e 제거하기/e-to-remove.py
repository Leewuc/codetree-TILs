n = input()
lst = list(n)
for i in range(len(n)):
    if lst[i] == 'e':
        lst.pop(i)
        break
nn = ''.join(lst)
print(nn)