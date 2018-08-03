from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unicodedata

#create firefox session
binary = FirefoxBinary('C:\\Users\\5002171\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
driver.implicitly_wait(30)

#go to google
driver.get("https://www.google.com")

#get search text box
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

#enter search keyword and submit
search_field.send_keys("opossum")
search_field.submit()

#get list of elements
lists = driver.find_elements_by_class_name("rc")

#get number of elements found
print("found --> ",len(lists))

i=0
for listitem in lists:
	try:
		listitem = listitem.get_attribute("innerHTML").encode('UTF-8', 'ignore')
		#print str(listitem.get_attribute("innerHTML"))
		print str(listitem)
	except:
		print "something wrong happened"
	i=i+1
	if(i>10):
		break

driver.quit()