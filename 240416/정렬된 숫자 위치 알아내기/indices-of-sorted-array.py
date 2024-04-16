# 길이 n 받기
n = int(input())

# 수열 입력값 받기
arr = list(map(int, input().split()))

# 수열이 순서대로 정렬된 리스트
sorted_arr = sorted(arr)

# 순서에 따라 번호 부여하기
sorted_arr_with_idx = []
for i in range(n):
    sorted_arr_with_idx.append((i + 1, sorted_arr[i]))

# sorted_arr과 값을 대조 -> 일치하면 번호값을 가져옴 
# 숫자 중복되면 먼저 나온 수열에 적은 값을 부여 -> sorted_arr_with_idx에서 해당 튜플값 삭제
for i in range(n):
    lens = len(sorted_arr_with_idx)
    
    for j in range(lens):
        # 동일한 값이 있으면 
        if arr[i] == sorted_arr_with_idx[j][1]:
            # 번호값을 출력하고
            print(sorted_arr_with_idx[j][0], end = " ")
            # 번호값이 있는 리스트에서 튜플을 삭제 
            sorted_arr_with_idx.pop(j)
            # 다음 수열로 넘어가기 
            break