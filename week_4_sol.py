from bs4 import BeautifulSoup
import re
import urllib.request
with urllib.request.urlopen("http://python-data.dr-chuck.net/comments_209059.html") as url:
    file = url.read()
	
soup =  BeautifulSoup(file,'html.parser')

tags = soup('span')
num = []

for tag in tags:
	tag = str(tag)
	item = re.findall('>([0-9]+)<',tag)
	if (len(item)>0):
		num.extend(item)

sum = 0
for val in num:
	sum = sum + int(val)
print (sum)


