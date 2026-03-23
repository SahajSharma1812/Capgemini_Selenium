from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


driver.get("https://www.amazon.in")
sleep(5)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Moai Statues")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.maximize_window()
driver.implicitly_wait(15)
sleep(5)
links = driver.find_elements(By.TAG_NAME,"img")
print(len(links))
print(links[5].text)



driver.quit()