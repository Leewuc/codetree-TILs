x,y = map(int,input().split())
ans = 0
for i in range(x,y+1):
    string_num = str(i)
    char_arr = list(string_num)
    int_arr = list(map(int,char_arr))
    digit_sum = sum(int_arr)
    ans = max(ans,digit_sum)
print(ans)