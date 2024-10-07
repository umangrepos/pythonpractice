import string

#s = "Hello test"
s = "The quick brown fox jumps over the lazy dog"

# SPACE = " "
# sets = set(s.lower())

# if SPACE in sets :
#     sets.remove(" ")

# print(sets == set(string.ascii_lowercase))

is_pangram = True

for char in string.ascii_lowercase :
    if char not in s.lower() :
        is_pangram = False
        break

print(is_pangram)



