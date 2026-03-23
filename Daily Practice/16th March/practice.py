from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options=ChromeOptions()
options.add_experimental_option('detach',True)
driver=Chrome(options=options)
driver.get('https://www.flipkart.com/search?q=rayban&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
driver.maximize_window()
sleep(3)
value=driver.find_element(By.XPATH,"//a[text()='Polarized Wayfarer Sunglasses (55)']/..//div[@class='hZ3P6w']").text
print(value)
sleep(10)
driver.quit()