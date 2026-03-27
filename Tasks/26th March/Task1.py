from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
import os
driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sa")
driver.find_element(By.ID,"login-button").click()
folder=os.path.join(os.getcwd(),'error-screenshot-11')
os.makedirs(folder,exist_ok=True)
expected='https://www.saucedemo.com/inventory.html'
actual=driver.current_url

assert expected==actual,driver.save_screenshot(f'{folder}/error__screenshot12.png')