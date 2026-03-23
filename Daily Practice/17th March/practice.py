# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
#
# o=ChromeOptions()
# o.add_experimental_option('detach', True)
# driver = Chrome(options=o)
#
# driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
# driver.find_element(By.XPATH, "//button[text()='Start']").click()
# driver.implicitly_wait(10)
# value=driver.find_element(By.ID,"finish").text
# print(value)


# driver.find_element(By.XPATH,"//button[text()='Start']").click()
# t=driver.find_element(By.XPATH,"//button[text()='Start']")
# driver.implicitly_wait(10)
# print(t.text)

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/mobile-phone-ab-at-store?pageUID=1773744239364")
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"nw1UBF v1zwn25").send_keys("mobile phones")
driver.find_element(By.XPATH,"//a[@href='https://www.decathlon.in/shop/Winter-Collection']").click()
driver.implicitly_wait(10)