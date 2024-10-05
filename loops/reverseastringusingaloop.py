string1 = "Test"

# for char in string1[::-1]:
#     print(char,end="")

# for char in reversed(string1):
#     print(char,end="")

for i in range(len(string1)-1,-1,-1):
    print(string1[i],end="")
