arr = list(map(int, input().split()))

while True:
    if arr.count(999) > 0:
        arr.remove(999)

    elif arr.count(-999) > 0:
        arr.remove(-999)
    
    else:
        break

max_val = max(arr);
min_val = min(arr);
print(max_val, min_val)