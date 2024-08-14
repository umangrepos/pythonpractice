file_path = "/home/umang/Downloads/pythonpractice/files/basicfile.txt"

filecontent = []

with open(file_path) as file :
    for line in file :
        filecontent.append(line)
    
print(filecontent)