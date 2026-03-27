from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://www.amazon.in")
driver.maximize_window()
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes")
sleep(2)
driver.find_element(By.XPATH,"//div[@aria-label='shoes for men casual']").click()
driver.find_element(By.XPATH,"//span[@class='a-button-text a-declarative']").click()
driver.find_element(By.XPATH,"//a[text()='Newest Arrivals']").click()
driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[3]").click()
el=driver.find_element(By.XPATH,"//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']")
print(el.text)
el1=driver.find_element(By.XPATH,"//span[@class='a-price-whole']")
print(el1.text)
