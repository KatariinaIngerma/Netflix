import urllib 
from selenium import *
from selenium import webdriver

sisend = "the 100"
driver = webdriver.Firefox(executable_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
driver.get(f'https://www.google.com/search?tbm=isch&q={sisend}')

driver.get(site)


driver.close()