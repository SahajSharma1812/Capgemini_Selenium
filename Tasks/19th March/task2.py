from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.implicitly_wait(15)


driver.find_element(By.ID, "singleFileInput").send_keys(r"/Users/sahajsharma/Downloads/69561.jpg")

