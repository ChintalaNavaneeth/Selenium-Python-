from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/")

logo = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a")
title = driver.title

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[5]/a").click()
driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[5]/ul/li[1]/a").click()
driver.find_element_by_name("Name").send_keys("XYZ sharma")
time.sleep(3)
driver.find_element_by_name("Email").send_keys("xyzsharma123@gmail.com")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[2]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]").click()
time.sleep(5)


driver.close()