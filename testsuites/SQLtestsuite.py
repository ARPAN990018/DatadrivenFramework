from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import mysql.connector
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.maximize_window()
con = mysql.connector.connect(host="localhost",user="root",password="Ab@ni123",database="employee")
curs = con.cursor()
curs.execute("select * from login")
for row in curs.fetchall():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(row[0])
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys(row[1])
    driver.find_element(By.XPATH,"//button[@id='submit']").click()
    if "Logged In Successfully" in driver.title:
        print("test passed")
        print(driver.title)
    else:
        print("test failed")
        print(driver.title)
    time.sleep(1)
con.close()
driver.close()


