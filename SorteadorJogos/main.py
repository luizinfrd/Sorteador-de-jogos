from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# abre o navegador
driver = webdriver.Chrome()
driver.get("https://sorteador.com.br/sorteio-de-nomes")
driver.maximize_window()
sleep(3)

# clica no sorteador de texto
driver.find_element(By.ID, "names").send_keys("Fortnite, Rocket league, FIFA, LEGO DC Super Villains, LEGO Star Wars, Cuphead")
sleep(3)

# clica em sortear agora
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/span/div/div/form/div[8]/button").click()
sleep(35)


