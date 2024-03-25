cnt = 0
while True :   
    if cnt == 3 :               #정상작동
        break
    n = int(input())    
    if cnt == 3 :               # 여기에 놓으면 EOFError 입력 값을 받은게 있는데 빠져나와서?
        break
    if n % 2 == 1 :
        continue
    else : 
        print(n//2)
        cnt += 1
    if cnt == 3 :               # 여기는 정상작동
        break