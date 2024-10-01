weight = int(input("please enter weight in kg: "))
height = int(input("please enter height in centemetr: "))

height= height/100

BMI = round((weight/height**2),2)

print(f"BMI: {BMI}")

print("your result is: ",end = "")

if BMI < 18.5:
    print("underweight")
elif (BMI == 18.5) or (BMI<=24.9):
    print("Normal")
elif 25 <= BMI <= 29.9:
    print("overweight")
else:
    print("obesity")

