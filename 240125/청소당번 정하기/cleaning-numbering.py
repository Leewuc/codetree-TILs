n = int(input())
g_c,b_c,h_c = 0,0,0
for i in range(1,n+1):
    if(i%12 == 0):
        h_c += 1
    elif(i%3 == 0):
        b_c += 1
    elif(i%2 == 0):
        g_c += 1
print(g_c, b_c, h_c)