my_dict = {"a":4,"b":4,"c":4}

my_uniqueset_len = len(set(my_dict.values()))

if my_uniqueset_len == 0 :
    print("empty")
elif my_uniqueset_len == 1 :
    print(True)
else :
    print(False)
