def findgcd(a,b):
    if b == 0:
        return a
    else:
        return findgcd(b,a%b)

print(findgcd(5,0))

# import math
# a=6
# b=2

# print(math.gcd(2,6))
