import datetime

date1input = input("date1: ")
date2input = input("date2: ")


date1list = date1input.split(" ")
year1 = int(date1list[0])
month1 = int(date1list[1])
day1 = int(date1list[2])

date1object = datetime.date(year1,month1,day1)

date2list = date2input.split(" ")
year2 = int(date2list[0])
month2 = int(date2list[1])
day2 = int(date2list[2])

date2object = datetime.date(year2,month2,day2)

if date2object < date1object :
    print("please enter valid date")

else:
    difference = (date2object - date1object).days

    print(f"the dayes are {difference}")
    
