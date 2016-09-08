import urllib.request
from bs4 import BeautifulSoup 
import re

url_inp = input('Enter url ')
if (len(url_inp)==0):
	exit()
count = input('Count: ')
if (len(count)==0): 
	exit() 
else: 
	count = int(count)
pos = input('Position: ')
if (len(pos)==0): 
	exit() 
else: 
	pos = int(pos)

print ('Retrieving: ',url_inp)

for i in range(1,count+1):
	with urllib.request.urlopen(url_inp) as url:
		html = url.read()
	soup = BeautifulSoup(html,'html.parser')
	link = soup('a') # extracts anchor tags or links as a list
	url_str = str(link[pos-1])
	url_link = re.findall('"(.*)"',url_str)
	url_inp = url_link[0]
	print ('Retrieving: ',url_inp)
	




	