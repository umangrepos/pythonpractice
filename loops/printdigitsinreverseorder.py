#option#1

num = 12345

# reverse = int(str(num)[::-1])


#option#2

reversed_num = 0

while num > 0 :
    reminder = num % 10 
    reversed_num = (reversed_num * 10 ) + reminder
    num = num // 10

print(reversed_num)



