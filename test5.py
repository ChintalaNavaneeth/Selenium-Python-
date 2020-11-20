from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.thesparksfoundationsingapore.org/")

logo = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a")
title = driver.title

driver.find_element_by_xpath("//*[@id='link-effect-3']/ul/li[6]/a").click()

driver.execute_script("window.scrollBy(0,440)","") #scrolling till 500 pixels
time.sleep(5)


driver.close()