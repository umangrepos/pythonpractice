height = 5

middlerow = (height+2)//2

for i in range(middlerow):
  print(" " * (middlerow-i),"*" * (i*2+1))
for i in range(middlerow-2,-1,-1):
  print(" " * (middlerow-i),"*" * (i*2+1))

