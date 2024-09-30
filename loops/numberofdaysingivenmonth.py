month = "february"

month_30_days = ("April","June","September","November")

month_31_days = ("January","March","May","July","August","October","December")


if month in month_30_days:
    print(f"{month} has 30 days")
elif month in month_31_days :
     print(f"{month} has 31 days")
else:
     print(f"{month} has 28 days")