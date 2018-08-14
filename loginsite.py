from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

binary = FirefoxBinary('C:\\Users\\5002171\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
driver.implicitly_wait(300)

driver.get("https://repository.xchanging.com/web/")

delay = 60

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'widget_nativeRepositoryPluginDojo_IMRLayout_0_LoginPane_XCusername')))
    print "Page is ready!"
    driver.find_element_by_id('nativeRepositoryPluginDojo_IMRLayout_0_LoginPane_XCusername').send_keys("user1")
    driver.find_element_by_id('nativeRepositoryPluginDojo_IMRLayout_0_LoginPane_XCusername2').send_keys("user2")
    driver.find_element_by_id('nativeRepositoryPluginDojo_IMRLayout_0_LoginPane_password').send_keys("password")
    driver.find_element_by_id('nativeRepositoryPluginDojo_IMRLayout_0_LoginPane_password').send_keys(Keys.RETURN)

except TimeoutException:
    print "Loading took too much time!"
    exit()




#driver.quit()