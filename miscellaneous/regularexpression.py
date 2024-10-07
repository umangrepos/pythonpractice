import re

regex = "^My[\w\s]+blue$"

string1 = input("enter string: ")

if re.search(regex,string1):
    print("match")
else:
    print("no match")