from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(15)

links = driver.find_elements(By.TAG_NAME, "a")

for i in links:
    print(i.text)


driver.quit()