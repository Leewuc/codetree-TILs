while True:
    n1 = input()
    arr = n1.split()
    a = int(arr[0])
    b = int(arr[1])
    c = str(arr[2])
    print(a*b)
    if(c == 'C'):
        break