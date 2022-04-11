from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


cont=1

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios")

sleep(2)

titulos = driver.find_elements(By.TAG_NAME,'li')

for i in titulos:
    print(f"Carro número {cont}:")
    print(i.text)
    cont = cont+1
