is_prime = True

n = int(input("enter an integer: "))

if n == 1:
    is_prime = False
else:
    for i in range(2,n):
        if i % 2 == 0 :
            is_prime = False
            break

if is_prime:
    print("prime")
else:
    print("not prime")




