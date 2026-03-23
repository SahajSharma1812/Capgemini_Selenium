from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


o=ChromeOptions()
o.add_experimental_option("detach",True)

#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.amazon.in")
sleep(1)
dropdown = driver.find_element(By.ID,"state")
option= Select(dropdown)
option.select_by_value("MH")
sleep(2)
option.select_by_index(0)
sleep(2)
dropdown2 = driver.find_element(By.ID,"hobby")
option2 = Select(dropdown2)
option2.select_by_index(0)
option2.select_by_index(2)
sleep(2)
option2.deselect_by_index(0)