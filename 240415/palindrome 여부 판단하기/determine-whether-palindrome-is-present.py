def palin(string):
    string1 = string[::-1]
    if string == string1:
        return "Yes"
    else:
        return "No"
string = input()
print(palin(string))