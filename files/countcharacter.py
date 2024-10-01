file_path = "/home/umang/Downloads/pythonpractice/files/famousquotes.txt"

charactercount = 0

with open(file_path) as file:
    for line in file:
        charactercount += len(line.replace(" ","").strip("\n"))

print(charactercount)