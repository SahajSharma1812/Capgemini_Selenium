from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()
sleep(5)
actions = ActionChains(driver)

# Mouse Hovering
ele1=driver.find_element(By.XPATH, "//button[@class='dropbtn']")

# Double Click
ele2=driver.find_element(By.XPATH, "//button[text()='Copy Text']")

# Drag and Drop
drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
drop=driver.find_element(By.XPATH,"//div[@id='droppable']")

actions.move_to_element(ele1).perform()
actions.double_click(ele2).perform()
actions.drag_and_drop(drag,drop).perform()
sleep(5)
driver.close()