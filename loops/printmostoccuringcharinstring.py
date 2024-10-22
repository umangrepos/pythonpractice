s = "helloo"
dicA={}
setA=set()

for i in s:
    if i in dicA:
        dicA[i] += 1
    else:
        dicA[i]=1

for i in dicA.values():
    setA.add(i)


n=max(setA)
for key,value in dicA.items():
    if value==n:
        print(key)