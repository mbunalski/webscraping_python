import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\Bun\\Desktop\\College\\Python\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")