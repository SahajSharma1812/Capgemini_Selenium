from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
expected='https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers'
driver.get('https://amazon.in')
sleep(2)
driver.find_element(By.XPATH,'(//a[@class="nav-a  "])[4]').click()
actual=driver.current_url
assert actual==expected, "You are on the wrong page move."
sleep(10)
driver.quit()
