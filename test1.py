from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get("https://www.thesparksfoundationsingapore.org/")

logo = driver.find_element_by_xpath("//*[@id='home']/div/div[1]/h1/a")
title = driver.title
