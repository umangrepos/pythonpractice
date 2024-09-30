def countvowel(string):
    string = string.lower()

    if not string :
        return 0
    elif string[0] in ("a","e","i","o","u"):
        return 1 + countvowel(string[1:])
    else:
        return countvowel(string[1:])
    
print(countvowel("Test"))