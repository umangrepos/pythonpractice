year = 1836

# if year % 4 == 0 :
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is a common year")
#     else:
#         print(f"{year} is a leap year")

# else:
#     print(f"{year} is a common year")


# option 2
# if year % 400 == 0:
#     print(f"{year} is a leap year")
# elif year % 100 == 0:
#     print(f"{year} is not a leap year")
# elif year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


#option 3
if year % 4 != 0:
    print(f"{year} is not a leap year")
elif year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 400 != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")


