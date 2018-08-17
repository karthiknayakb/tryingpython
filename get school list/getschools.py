import urllib2
from bs4 import BeautifulSoup
link = "http://www.manchester.gov.uk/directory/84/school_finder/category/605"

page = urllib2.urlopen(link)
soup = BeautifulSoup(page,"lxml")
table = soup.find("ul",{"class":"no-list"})
a = table.findAll('a')
# m = 0;
#shareLinks = []
par = "http://www.manchester.gov.uk"
file = open("schoolLinks.csv","w")
for school in a:
	file.write(par+school['href']+"\n")
	# m+=1
	# if m>=5:
	# 	break
file.close()

# 
# for tr in a:
# 	cols = tr.findAll('td')
# 	for td in cols:
# 		a = td.find('a',href=True)
# 		file.write(str(a.find(text=True))+","+str(a['href'])+"\n")
# 		m+=1
# #print shareLinks
# print "shareLinks = ",m
