import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\Users\\Bun\\Desktop\\College\\Python\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.amazon.com/Acer-SB220Q-Ultra-Thin-Frame-Monitor/dp/B07CVL2D2S/ref=sr_1_3?dchild=1&keywords=monitor&qid=1615835704&sr=8-3")
