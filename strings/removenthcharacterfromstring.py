s = "test"

n=2

newstr = ""

if (not s) or (n >= len(s)) :
    print(s)
else :
    for i in range (len(s)):
        if i != n :
            newstr += s[i]
print(newstr)