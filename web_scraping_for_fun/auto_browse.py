from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\dev\chromedriver\chromedriver.exe"

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome()

driver.get('https://www.amazon.com')
#price_whole = driver.find_element(By.CLASS_NAME, 'a-price-whole')
#price_fraction = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
#print(f'The price is: ${price_whole.text}.{price_fraction.text}')

# //*[@id="twotabsearchtextbox"]

basics = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[5]')
basics.click()

#search_bar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
#print(search_bar.tag_name)

# driver.quit()
