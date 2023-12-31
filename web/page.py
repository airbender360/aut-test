from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page:
    driver_path = r'C:\Users\063\Desktop\backupScripts\tools\chromedriver.exe'
    service = Service(driver_path)
    global driver
    driver = webdriver.Chrome(service=service)
    
    def open(self, url):
        driver.maximize_window()
        return driver.get(url)
    
    def quit(self):
        return driver.quit()
    
    #Si el parámetro es 0 recibe un css selector, sino recibe un xpath
    def getElement(self, par, locator):
        elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator))) if par == 0 else WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        return elemento