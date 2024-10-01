List1=["a","a","b","c","a","b"]

freqdict = {}

for elem in List1:
    if elem not in freqdict:
        freqdict[elem] = 1
    else:
        freqdict[elem] += 1

print(freqdict)