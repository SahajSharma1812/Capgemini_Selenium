from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send

o=ChromeOptions()
o.add_experimental_option("detach",True)

#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# sleep(2)
# driver.maximize_window()
# sleep(1)
#
# # ele=driver.find_element(By.ID,"doubleClickBtn")
#
#
#
#
# ele2=driver.find_element(By.ID,"rightClickBtn")
#
# # ele3=driver.find_element(By.XPATH,"//button[text()='Click Me']").click()
# action=ActionChains(driver)
# action.context
#_click(ele2).perform()
# sleep(3)
# driver.quit()
sleep(2)

la = driver.find_element(
    By.XPATH, "//img[contains(@alt,'Aquaminder Smart Water Bottle')]"
)
action=ActionChains(driver)

# action.scroll_to_element(la).pause(3).perform()
action.scroll_by_amount(delta_x=0,delta_y=900).perform()
sleep(10)
driver.quit()