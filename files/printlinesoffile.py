file_path = "/home/umang/Downloads/pythonpractice/files/basicfile.txt"
n = int(input("how many lines would you like to read?: "))




with open(file_path) as file :
    lines = file.readlines()
    number = len(lines)

    if number < n :
        print(f"please enter a valid value file has {number} of lines")
    else :
        for i in range(n):
            print(lines[i].strip("\n"))

    
