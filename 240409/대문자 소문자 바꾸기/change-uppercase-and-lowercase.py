string = input()

new_string = ""
for char in string:
    if char >= 'A' and char <= 'Z':
        new_string += chr(ord(char) - ord('A') + ord('a'))
    else:
        new_string += chr(ord(char) - ord('a') + ord('A'))

print(new_string)