from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

#create firefox session
# try:
options = Options()
options.set_headless(headless=True)
binary = FirefoxBinary('C:\\Users\\5002171\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary,firefox_options=options)
print("Firefox Headless Browser Invoked")
driver.get('https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt')
# res = driver.find_element_by_xpath("//*")
# source_code = res.get_attribute("outerHTML")
page = driver.page_source
soup = BeautifulSoup(page,"lxml")
print type(page)
#print page
ips = soup.find("pre")
print [str(i) for i in ips.getText().strip().split("\n")]
driver.quit()
# except:
# 	print "something wrong happened"
# 	driver.quit()