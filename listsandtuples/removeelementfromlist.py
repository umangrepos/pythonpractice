List1 = [3,4,5,6]
element_to_remove = 7


if not List1 :
    print("empty list")
elif List1.count(element_to_remove) == 0:
    print("not found")

else:
    for i in range(List1.count(element_to_remove)) :
        List1.remove(element_to_remove)

print(List1)