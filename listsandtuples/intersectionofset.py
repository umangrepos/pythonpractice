set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

intersection = set()

for elem in set1 :
    if elem in set2:
        intersection.add(elem)
print(intersection)


#print(set1.intersection(set2))


#for multiple set
#print(set1.intersection(set2,set3))
