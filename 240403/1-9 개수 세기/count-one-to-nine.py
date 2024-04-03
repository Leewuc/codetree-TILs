from typing import List

def int_cnt(arr : List[int], new_arr : List[int]) -> List[int]:
    for elem in arr:
        new_arr[elem] += 1
    return new_arr

n = int(input())

arr = list(map(int, input().split()))
new_arr = [0] * 100
cnt_arr = int_cnt(arr, new_arr)
for i in range(1, 10):
    print(cnt_arr[i])