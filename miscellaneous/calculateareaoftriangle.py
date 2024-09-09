base = int(input("enter the base:"))
height = int(input("enter the height:"))

if base > 0 and height > 0 :
    area = round((base * height)/2,2)
    print(area)

else :
    print("please enter correct value")
    