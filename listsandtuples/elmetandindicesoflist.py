List2 = [1,2,3,4]

List1 = ["a","b","c"]

#if len(List1) == 0 :
#    print("empty list")
#else:
#     for i in range(len(List1)):
#          print(List1[i],i)

if not List1:
    print("empty list")
else:
    for i , elem in enumerate(List1) :
        print(elem,i)

