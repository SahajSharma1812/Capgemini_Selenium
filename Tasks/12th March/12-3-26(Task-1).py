from selenium.webdriver import Chrome, ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get("https://www.google.com")
print(driver.title)
