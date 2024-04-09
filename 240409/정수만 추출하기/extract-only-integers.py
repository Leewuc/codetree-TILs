a, b = input().split()

# 빈 문자열 만들기 
new_a = ""
new_b = ""
 
# 숫자인 경우 새로운 문자열에 추가
for char in a:
    if not char.isdecimal():
        break
  
    new_a += char

for char in b:
    if not char.isdecimal():
        break
    
    new_b += char

# 문자열 정수화 
new_a = int(new_a)
new_b = int(new_b)

# 합계 구하기
print(new_a + new_b)