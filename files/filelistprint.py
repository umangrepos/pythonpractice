file_path = "/home/umang/Downloads/pythonpractice/files/basicfile3.txt"

my_list=[1,2,3,4,5]

with open(file_path,"w") as file:
    for elem in my_list:
        file.write(str(elem)+"\n")


