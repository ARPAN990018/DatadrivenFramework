import re
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilityfolder import LoanUtils
import time

path = "C:\\Users\\RIC\\PycharmProjects\\DatadrivenFrameworkProject\\testdata\\DataforLoansite1.xlsx"
driver = webdriver.Chrome()
driver.get("https://www.kviconline.gov.in/pmegpeportal/jsp/emiCalculator.jsp")
driver.maximize_window()
driver.implicitly_wait(10)

numberofrow = LoanUtils.rownumber(path,"Sheet1")
print(numberofrow)
numberofColumn = LoanUtils.columnnumber(path,"Sheet1")
print(numberofColumn)

for r in range(2,numberofrow+1):
    amount = LoanUtils.readdata(path,"Sheet1",r,1)
    driver.find_element(By.XPATH,"//input[@id='amount']").clear()
    driver.find_element(By.XPATH,"//input[@id='amount']").send_keys(amount)

    rateofinterest = LoanUtils.readdata(path,"Sheet1",r,2)
    driver.find_element(By.XPATH, "//input[@id='apr']").clear()
    driver.find_element(By.XPATH,"//input[@id='apr']").send_keys(rateofinterest)

    year = LoanUtils.readdata(path,"Sheet1",r,3)
    teneure = Select(driver.find_element(By.XPATH,"//select[@id='tenure']"))
    teneure.select_by_visible_text(str(year))

    driver.find_element(By.XPATH,"//button[@id='calculation']").click()
    time.sleep(3)
    expectedEMI = LoanUtils.readdata(path,"Sheet1",r,4)

    emi_amount = driver.find_element(By.XPATH,"//div[@class='right']//div").text
    emi = re.search(r'\d+', emi_amount).group()
    LoanUtils.writedata(path,"Sheet1",r,5,emi)
    if float(emi) == float(expectedEMI):
        LoanUtils.writedata(path,"Sheet1",r,6,"passed")
    else:
        LoanUtils.writedata(path,"Sheet1",r,6,"failed")
