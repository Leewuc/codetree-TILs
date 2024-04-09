n = input()
arr = list(n)
arr[1] = 'a'
arr[-2] = 'a'
n = ''.join(arr)
print(n)