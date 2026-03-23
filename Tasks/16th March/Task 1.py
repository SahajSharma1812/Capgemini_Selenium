from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options=ChromeOptions()
options.add_experimental_option('detach',True)
driver=Chrome(options=options)
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(3)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('Mobile Phones')
sleep(3)
driver.find_element(By.ID,'nav-search-submit-button').click()
sleep(3)
value=driver.find_element(By.XPATH,"//span[text()='iPhone 17 Pro Max 2 TB: 17.42 cm (6.9″) Display with Promotion, A19 Pro Chip, Best Battery Life in Any iPhone Ever, Pro Fusion Camera System, Center Stage Front Camera; Silver']/../../../..//span[@class='a-price-whole']").text
print(value)
sleep(10)
driver.quit()