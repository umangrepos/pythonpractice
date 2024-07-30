s = "stringtest"
newstr = ""


# for i in range(len(s)):
#     if i % 2 !=0 :
#         newstr += s[i]

for i in range(1,len(s),2) :
    newstr += s[i]

print(newstr)

#for checking string is numeric or not use s.isdecimal() method it will return boolean value