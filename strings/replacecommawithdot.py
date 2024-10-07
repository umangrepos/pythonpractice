s = "Hello, Word!"
news = ""

comma = ","
dot = "."

for i in s :
    if i == comma :
        news += dot
    else :
        news += i

print(news)