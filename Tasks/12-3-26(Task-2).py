from selenium.webdriver import Chrome, ChromeOptions
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get("https://www.youtube.com")
print(driver.current_url)