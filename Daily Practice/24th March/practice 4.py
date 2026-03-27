from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
# options.add_experimental_option("prefs",{"safebrowsing.enabled":True})
sleep(2)
driver.find_element(By.XPATH,'(//a[@href="https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe"])[2]').click()