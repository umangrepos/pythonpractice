file_path = "/home/umang/Downloads/pythonpractice/files/famousquote.txt"
copy_path = "/home/umang/Downloads/pythonpractice/files/famousquotecopy.txt"

with open(file_path) as file , open (copy_path , "w") as copy:
    for line in file:
        copy.write(line)