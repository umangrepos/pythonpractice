List1 = [3,3,4,4,5,5,6,6]

#noduplicates = list(set(List1))

#print(noduplicates)

noduplicates = list(dict.fromkeys(List1))

print(noduplicates)