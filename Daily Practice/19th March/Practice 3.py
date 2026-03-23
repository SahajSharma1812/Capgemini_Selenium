from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(10)

driver.find_element(By.ID,"firstName").send_keys("Sahaj")
driver.find_element(By.ID,"lastName").send_keys("Sharma")
driver.find_element(By.ID,"userEmail").send_keys("ajsahajsharma@gmail.com")
driver.find_element(By.CLASS_NAME,"form-check.form-check-inline").click()
sleep(2)
driver.find_element(By.ID,"userNumber").send_keys("7456244234")
driver.find_element(By.ID,"dateOfBirthInput").send_keys("18 Dec 2004")
driver.find_element(By.CLASS_NAME,"subjects-auto-complete__input-container.css-19bb58m").send_keys("Math")
driver.find_element(By.CLASS_NAME,"form-check-label").click()
driver.find_element(By.ID,"currentAddress").send_keys("Jaipur")
driver.quit()
