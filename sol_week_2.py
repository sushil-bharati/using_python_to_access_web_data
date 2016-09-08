import re
hand = open('test1.txt')
num = []
for line in hand:
	line = line.rstrip()
	found = (re.findall('[0-9]+',line))
	if (len(found)>0):
		num.extend(found)
sum = 0
for val in num:
	sum = sum + int(val)
print (sum)

