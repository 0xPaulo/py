from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium. webdriver. common. keys import Keys
import time
driver = webdriver.Chrome(
    executable_path=r'C:\Users\Paulo\vs\python\automatize tarefas\py\Automatizando tarefas\chromedriver.exe')
driver.get('https://www.tumblr.com/dashboard')
time.sleep(1)
# 1 //*[@id="Get started"]/div/div/div[2]/div[1]/section/div/form/div[1]/input
# 2 //*[@id="Get started"]/div/div/div[2]/div[1]/section/div/form/div[2]/input
# 3 //*[@id="Get started"]/div/div/div[2]/div[1]/section/div/form/button/span
email = driver.find_element(
    By.XPATH, '//*[@id="Get started"]/div/div/div[2]/div[1]/section/div/form/div[1]/input')
senha = driver.find_element(
    By.XPATH, '//*[@id="Get started"]/div/div/div[2]/div[1]/section/div/form/div[2]/input')
login = driver.find_element(
    By.XPATH, '//*[@id="Get started"]/div/div/div[2]/div[1]/section/div/form/button/span')
email.send_keys("caoslpure@gmail.com")
senha.send_keys("J&nD3)e)J6emPn")
time.sleep(1)
login.click()
time.sleep(5)
driver.get('https://www.tumblr.com/new/photo?context=queue&name=inugamidoo')

