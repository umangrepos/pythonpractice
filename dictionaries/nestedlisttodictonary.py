my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
new_dictionary = {}

for nested_list in my_list:
    key = nested_list[0]
    value = nested_list[1]
    new_dictionary[key] = value

print(new_dictionary)

