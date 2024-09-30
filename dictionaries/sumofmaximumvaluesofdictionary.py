my_dict = {
   	"a": [1, 2, 3],
   	"b": [4, 0, -4],
   	"c": [3, 5, 9],
   	"d": [45, 12, 100]
}

maxsum = 0

for values in my_dict.values():
    listsum = sum(values)

    if maxsum < listsum:
    
        maxsum = listsum

print(maxsum)