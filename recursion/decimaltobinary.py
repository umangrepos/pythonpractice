def convert_to_binary(decimalnum):
    if decimalnum == 0:
        return '0'
    else:
        return (convert_to_binary(decimalnum//2)+ str(decimalnum%2)).lstrip("0") 
    
print(convert_to_binary(5))

