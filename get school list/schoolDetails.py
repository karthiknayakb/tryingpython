import urllib2
from bs4 import BeautifulSoup
link1 = ["http://www.manchester.gov.uk/directory_record/261366/abraham_moss_community_school/category/605/all_schools",
"http://www.manchester.gov.uk/directory_record/261421/heald_place_primary_school/category/605/all_schools",
"http://www.manchester.gov.uk/directory_record/261449/meade_hill_school/category/605/all_schools"]


import re

# 1. Link to the schools website
schoolweb = re.compile("^School website$",re.IGNORECASE)
# 2. Name of school
school = re.compile("^school$",re.IGNORECASE)
# 3. Contact number of school
tphone = re.compile("^Telephone number$",re.IGNORECASE)
# 4. Contact name listed
hmname = re.compile("^Headteacher/Principal",re.IGNORECASE)
# 5. what their title is (e.g. head teacher)
#"Headteacher/Principal"
#Email
email = re.compile("^email[a-z]*[A-Z]*[a-z]*",re.IGNORECASE)

def getSchoolDetails(link):
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page,"lxml")
	record = soup.find("ol",{"class":"record-list"})
	lis = record.findAll("li")
	sdic = {}
	n = 0
	for li in lis:
		try:
			h = li.find("h4").find(text=True)
			if schoolweb.match(h):
				#print li.find("p").find(text=True)
				sdic[h] = li.find("p").find(text=True)
				n+=1
			if school.match(h):
				#print li.find("p").find(text=True)
				sdic[h] = li.find("p").find(text=True)
				n+=1
			if tphone.match(h):
				#print li.find("p").find(text=True)
				sdic[h] = li.find("p").find(text=True)
				n+=1
			if hmname.match(h):
				#print li.find("p").find(text=True)
				sdic[h] = li.find("p").find(text=True)
				n+=1
			if email.match(h):
				#print li.find("p").find(text=True)
				sdic[h] = li.find("p").find(text=True)
				n+=1
			if n>=5:
				break
		except:
			print "error occured while checking "+li
	sdic["sourcelink"] = link
	return sdic

def getSchoolFile():
	file = open("schools.csv","w")
	for i in link1:
		sarr = []
		ldic = getSchoolDetails(i)
		#print ldic
		if("School website" in ldic):
			sarr.append(str(ldic["School website"]))
		else:
			sarr.append('na')
		if("School" in ldic):
			sarr.append(str(ldic["School"]))
		else:
			sarr.append('na')
		if("Telephone number" in ldic):
			sarr.append(str(ldic["Telephone number"]).replace("<br>",""))
		else:
			sarr.append('na')
		if("Headteacher/Principal" in ldic):
			sarr.append(str(ldic["Headteacher/Principal"]))
		else:
			sarr.append('na')
		if("Email" in ldic):
			sarr.append(str(ldic["Email"]).replace("<br>",""))
		else:
			sarr.append('na')
		#print [ldic["School website"],ldic["School"],ldic["Telephone number"],ldic["Headteacher/Principal"],ldic["Email"]]
		sarr.append(str(ldic["sourcelink"]))
		#print sarr
		#print ",".join(sarr)
		file.write(",".join(sarr))
		file.write("\n") 
#getSchoolFile()

print getSchoolDetails("http://www.manchester.gov.uk/directory_record/261520/st_marys_cofe_primary_school_moss_side/category/605/all_schools")