my_dict = {
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
}

#sort is used when we have to modify original list
#sorted is used to make a new copy of dictionary without modifying original one

for list in my_dict.values():
    list.sort()

print(my_dict)