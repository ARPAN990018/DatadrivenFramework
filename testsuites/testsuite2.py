import time
import os
import openpyxl
from utilityfolder import dataUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = os.path.join(os.getcwd(), "testdata", "datafortesting.xlsx")
rownum = dataUtils.rownumber(path,"Sheet1")
columnnum = dataUtils.columnnumber(path,"Sheet1")
print(rownum)
print(columnnum)
op = webdriver.ChromeOptions()
op.add_argument("--headless")
driver = webdriver.Chrome(options=op)
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
n = 1
while n <= 11:
    data = (WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f"(//a[@class='nav-a  '])[{n}]"))).text)
    dataUtils.writedata(path,"Sheet1",n+1,1,data)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"(//a[@class='nav-a  '])[{n}]"))).click()
    num = len(driver.find_elements(By.TAG_NAME,"a"))
    ref = dataUtils.readdata(path, "Sheet1", n + 1, 2)
    dataUtils.writedata(path, "Sheet1", n + 1, 3, num)
    if ref == num:
        dataUtils.writedata(path, "Sheet1", n + 1, 4, "passed")
    else :
        dataUtils.writedata(path, "Sheet1", n + 1, 4, "failed")
    driver.back()
    n = n + 1


