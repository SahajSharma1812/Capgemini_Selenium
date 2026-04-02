from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
sleep(2)
def test_gender():
    driver.find_element(By.ID,"gender-male").click()
    sleep(1)
def test_firstname():
    driver.find_element(By.ID,"FirstName").send_keys("Sahaj")
    sleep(1)
def test_lastname():
    driver.find_element(By.ID,"LastName").send_keys("Sharma")
def test_email():
    driver.find_element(By.ID,"Email").send_keys("ajsahajsharma@gmail.com")
def test_password():
    driver.find_element(By.ID,"Password").send_keys("qwertyuiop")
def test_confirmpass():
    driver.find_element(By.ID,"ConfirmPassword").send_keys("qwertyuiop")
def test_submit():
    driver.find_element(By.ID,"register-button").click()