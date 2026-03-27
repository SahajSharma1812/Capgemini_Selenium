from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("file:///Users/sahajsharma/PycharmProjects/PythonProject/Selenium/Daily%20Practice/24th%20March/page1.html")
sleep(3)
driver.find_element(By.ID,"input").send_keys("please please please")
driver.switch_to.frame('dareal')
sleep(2)
driver.find_element(By.ID,"inp2").send_keys("please please please")
driver.switch_to.frame('dareall')
sleep(2)
driver.find_element(By.ID,"inp3").send_keys("please please please")



