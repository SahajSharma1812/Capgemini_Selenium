
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get('https://x.com/')
driver.switch_to.frame(0)
driver.find_element(By.CLASS_NAME,'nsm7Bb-HzV7m-LgbsSe-BPrWId').click()