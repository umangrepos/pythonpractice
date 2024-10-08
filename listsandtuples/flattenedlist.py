List1=[[1,2,3],[4,5,6],[7,8,9]]

flattenedlist = []

for elem in List1:
    if isinstance(elem,list):
        for nestedelem in elem:
            flattenedlist.append(nestedelem)
    else:
        flattenedlist.append(elem)

print(flattenedlist)