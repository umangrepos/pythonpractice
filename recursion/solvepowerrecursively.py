def calculatepower(a,b):
    if b == 1:
        return a
    else :
        return a * calculatepower(a,b-1)
    
