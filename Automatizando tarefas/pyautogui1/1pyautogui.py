import pyautogui
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium. webdriver. common. keys import Keys
import time
driver = webdriver.Chrome(
    executable_path=r'C:\Users\Paulo\vs\python\automatize tarefas\py\Automatizando tarefas\chromedriver.exe')
driver.get('https://www.tumblr.com/dashboard')
time.sleep(1)

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
time.sleep(3)

pyautogui.click(x=1015, y=175,duration=1.2) #pessoa
pyautogui.click(x=941, y=676,duration=1.2) #perfil
pyautogui.click(x=859, y=537,duration=1.2) #fila
time.sleep(20)
pyautogui.click(256,502,duration=0.5) #foto
time.sleep(15)
pyautogui.click(429,353,duration=0.5) #carregar imagem
time.sleep(3)
pyautogui.click(x=483, y=333, clicks=2,duration=0.5) #pasta 1
time.sleep(1)
pyautogui.click(x=483, y=333, clicks=2,duration=0.5) #pasta 2
time.sleep(1)
pyautogui.click(246,175, clicks=2,duration=0.5)
time.sleep(20) #espera imagem carregar 

#pagedown
body = driver.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)

time.sleep(1)
pyautogui.click(762,618,duration=1)    #post

#-------------------apagando---------------------------------
for filename in sorted(os.listdir("C:/Users/Paulo/Pictures/Saved Pictures"))[:1]:
    filename_relPath = os.path.join("C:/Users/Paulo/Pictures/Saved Pictures",filename)
    os.remove(filename_relPath)
#---------------------------------------------------

#------------------Loop---------------------------
time.sleep(2)
pyautogui.click(256,502,duration=1) #foto
time.sleep(3)
pyautogui.click(429,353,duration=1) #carregar imagem
time.sleep(1)
pyautogui.click(246,175, clicks=2,duration=0.5)
time.sleep(20) #espera imagem carregar 
body = driver.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
pyautogui.click(762,618,duration=1)
#---------------------------------------------

