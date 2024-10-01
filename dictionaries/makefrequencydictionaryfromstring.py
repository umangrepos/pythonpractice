string1="Hello"
string1 = string1.lower()

frequencydict = {}

for char in string1:
    if char.isalpha():
        if char in frequencydict:
            frequencydict[char] +=1
        else:
            frequencydict[char] =1

print(frequencydict)