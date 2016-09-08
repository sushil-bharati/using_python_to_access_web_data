import urllib.request
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    #There are some changes done here as I run Python 3.5.2
	#Open the given url using urllib.request 
    with urllib.request.urlopen(address) as url:
        data= url.read()
    
    print ('Retrieved',len(data),'characters')
    
	#parse XML
    tree = ET.fromstring(data)
    #get all the <comment> tags
    counts = tree.findall('.//comment')
    
    sum = 0
    for item in counts:
        sum = sum + int(item.find('count').text)

    print ('sum',sum)
  