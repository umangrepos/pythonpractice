#is_prime = True

n = int(input("enter an integer: "))

#if n==0 or n == 1:
#    is_prime = False
#else:
#    for i in range(2,n):
#         if n % i == 0 :
#             is_prime = False
#             break
# if is_prime:
#     print("prime")
# else:
#     print("not prime")





if n==0 or n == 1:
   print("not prime")
else:
    for i in range(2,n):
        if n % i == 0 :
            print("not prime")
            break
        
    else:
        print("prime")  


