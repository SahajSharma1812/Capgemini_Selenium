from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("http://127.0.0.1:5500/Frames_Selenium(Page-1).html")
sleep(2)
driver.find_element(By.ID, "input").send_keys("Wallah")

driver.switch_to.frame('name1')             # This is the switch by using Name
# driver.switch_to.frame(0)                   # This is the switching by using index (Here we used 0 because this is the first page in action for the main page)
driver.find_element(By.ID, "input2").send_keys("habi")
driver.switch_to.frame('name2')
# driver.switch_to.frame(0)                   # In page 3 we again used page 0 because currently we are on Page 2 and approaching from this will need 0.
driver.find_element(By.ID, "input3").send_keys("biii")
# driver.switch_to.parent_frame()             
driver.switch_to.default_content()           # This is used to go back to the main default parent.
sleep(3)

driver.find_element(By.ID, "input").send_keys("  Wallah")