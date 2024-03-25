total_age = 0
count = 0

while True:
    age = int(input())
    if age // 10 != 2:
        break
    total_age += age
    count += 1

if count == 0:
    print("No age entered")
else:
    average_age = total_age / count
    print(f'{average_age:.2f}')