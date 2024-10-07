def printpattern(n):
    if n ==1 :
        print("*")
    else:
        print("*" * n)
        printpattern(n-1)

printpattern(6)

