from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
import os
driver.get("https://www.lenskart.com/")
driver.maximize_window()
driver.find_element(By.ID,"lrd1").click()
expected='https://www.lenskart.com/eyeglasses.html'
actual=driver.current_url
assert expected==actual,"URL MISMATCHED"
dropdown=driver.find_element(By.ID,"sortByDropdown")
option=Select(dropdown)
option.select_by_index(5)
folder=os.path.join(os.getcwd(),'Lenskart')
os.makedirs(folder,exist_ok=True)
driver.save_screenshot(f'{folder}/Lenskart_Page.png')