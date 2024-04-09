n,m = input().split()
print(ord(n)+ord(m),end=" ")
if n > m:
    print(ord(n)-ord(m))
else:
    print(ord(m)-ord(n))