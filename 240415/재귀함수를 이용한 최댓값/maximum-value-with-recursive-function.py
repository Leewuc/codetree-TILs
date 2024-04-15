def find_max_recursive(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_rest = find_max_recursive(arr, n - 1)
        return max(max_rest, arr[n - 1])

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 최대값 찾아서 출력
print(find_max_recursive(arr, n))