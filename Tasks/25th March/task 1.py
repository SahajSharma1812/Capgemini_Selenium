from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID,'user-name').send_keys('admin')
driver.find_element(By.ID,'password').send_keys('holla')
driver.find_element(By.ID,'login-button').click()
expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url
if expected == actual:
    pass
else:
    driver.save_screenshot('screenshot2.png')