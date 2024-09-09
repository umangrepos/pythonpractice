file_path = "/home/umang/Downloads/pythonpractice/files/basicfile2.txt"
longestword = ""

with open(file_path) as file :
    for line in file :
        if len(line) > len(longestword) :
            longestword = line
    
print(longestword)