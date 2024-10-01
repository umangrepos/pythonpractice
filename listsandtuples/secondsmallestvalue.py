List1 = [3,4,5,6]

# if len(List1) > 1:
#     sorted_list = sorted(List1)
#     print(sorted_list[1])
# else:
#     print(None)

if len(List1) > 1:
    noduplicates = set(List1)
    noduplicates.remove(min(noduplicates))
    print(min(noduplicates))
else:
    print(None)