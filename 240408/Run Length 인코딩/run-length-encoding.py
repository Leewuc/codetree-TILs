s=input()
string=''

# 입력의 첫번쨰 값 초기화
curr_char=s[0]
num_char=1

for target_char in s[1:]:
    if target_char==curr_char:
        num_char+=1
    else:
        string +=curr_char 
        string += str(num_char)

        curr_char=target_char 
        num_char = 1 

# 마지막 덩어리
string += curr_char 
string += str(num_char)


print(len(string))
print(string)