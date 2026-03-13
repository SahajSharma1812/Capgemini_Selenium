from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
a=ChromeOptions()
a.add_experimental_option("detach",True)

driver=Chrome(options=a)
driver.get("https://wikipedia.com")
sleep(2)
title=driver.title
print(title)
driver.get("https://amazon.in")
sleep(3)
title=driver.title
print(title)
driver.back()
driver.close()
