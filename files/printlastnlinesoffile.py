file_path = "/home/umang/Downloads/pythonpractice/files/basicfile.txt"

n = int(input("how many lines you want to print: "))

with open(file_path) as file :
    lines = file.readlines()
    num_lines = len(lines)

if num_lines < n :
    print("please enter correct value")
else :
    for i in range (-n,0):
        print(lines[i].strip("\n"))

