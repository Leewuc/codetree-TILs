def eve(n):
    if n % 2 == 0 and ((n//10)+(n%10)) % 5 == 0:
        return "Yes"
    else:
        return "No"
n = int(input())
print(eve(n))