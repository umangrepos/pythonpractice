import os.path

myfile = "famousquote.txt"

if os.path.isfile(myfile):
    print("exist")
else :
    print("not exist")
    print(os.path)