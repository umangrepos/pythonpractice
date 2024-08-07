s = "Hello"

repeated_chars = []

for char in s :
    if (s.count(char)>1) and (char not in repeated_chars) :
        repeated_chars.append(char)

print(len(repeated_chars))


# if len(repeated_chars) > 0 :
#     for char in sorted(repeated_chars):
#         print(char , end =" ")

# else :
#     print(None)

if repeated_chars :
        print(*sorted(repeated_chars),sep= "")
else :
    print(None)