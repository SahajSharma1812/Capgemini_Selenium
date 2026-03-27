from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/#")
sleep(2)
driver.maximize_window()
#---------------------I---------Simple ALert---------------
driver.find_element(By.ID, 'alertBtn').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
#-------------------II-------Confirmation Alert-------------------
driver.find_element(By.ID, 'confirmBtn').click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
# alert.dismiss()