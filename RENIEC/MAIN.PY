from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.reniec.gob.pe/portal/masServiciosLinea.htm')
driver.find_element(By.XPATH, '//a[contains(text(),"Peruanos en el Extranjero")]').click() 
time.sleep(1)
driver.find_element(By.XPATH, '//a[contains(text(),"CONSULADOS EN EL MUNDO")]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[contains(text(),"Lista de Consulados en el mundo")]').click()
time.sleep(1)

windows = driver.window_handles

driver.switch_to.window(windows[-1])

driver.find_element(By.XPATH, '//input[@id="txtSearch"]').send_keys("Cuenca")
driver.find_element(By.XPATH, '//img[@class="imgSearchLupa"]').click()

time.sleep(1)

driver.switch_to.window(windows[0])

time.sleep(5)