from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.thesparksfoundationsingapore.org/")


img  = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a")
title = driver.title

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[1]/ul/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[2]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[3]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[4]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[5]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[6]").click()
time.sleep(3)
driver.back()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/ul/li[7]").click()
driver.back()

driver.close()



