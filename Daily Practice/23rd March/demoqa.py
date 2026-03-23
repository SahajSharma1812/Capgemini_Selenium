from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send

o=ChromeOptions()
o.add_experimental_option("detach",True)

#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://demoqa.com/text-box")
sleep(5)
driver.maximize_window()
ele=driver.find_element(By.ID,"currentAddress")
ele.send_keys("None of your business.")
ele.send_keys(Keys.COMMAND,'a')
ele.send_keys(Keys.COMMAND,'c')
sleep(2)
ele2=driver.find_element(By.ID,"permanentAddress")
ele2.send_keys(Keys.COMMAND,'a')
ele2.send_keys(Keys.COMMAND,'v')

