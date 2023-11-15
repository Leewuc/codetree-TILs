i = input()
arr = i.split()
a = int(arr[0])
b = int(arr[1])
bmi = b*100*100//(a*a)
print(bmi)
if bmi >= 25:
    print("Obesity")