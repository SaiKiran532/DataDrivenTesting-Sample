from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtils  # this import class has all the methods related to Excel file access

# Excel data file path (Note: provide your existing file path)
path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject3\\DataDrivenTesting\\LoginData.xlsx"

driver = webdriver.Chrome()  # Or choose the appropriate webdriver for your browser
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(5)

rows = XLUtils.getRowCount(path, 'Sheet1')

for i in range(2, rows+1):
    email = XLUtils.readData(path, 'Sheet1', i, 1)  # reads the existing "email" from excel
    password = XLUtils.readData(path, 'Sheet1', i, 2)  # reads the existing "password" from excel
    driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    if driver.title == 'Automation Exercise':
        print("Testcase Passed ")
        XLUtils.writeData(path, 'Sheet1', i, 3, "Passed")  # writes the data into Excel as "Passed"
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    else:
        print("Testcase Failed")
        XLUtils.writeData(path, 'Sheet1', i, 3, "Failed")   # writes the data into Excel as "Failed"





